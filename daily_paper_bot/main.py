import os
import re  # 新增
import json
import requests
import time
from bs4 import BeautifulSoup
import arxiv
import pypdf
import markdown
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import merge_reports # 导入合并脚本

# 加载环境变量
load_dotenv()

# 配置
ARXIV_URL = "https://arxiv.org/list/eess.AS/recent"
OUTPUT_DIR = "reports"
PDF_DIR = "pdfs"
# 获取当前脚本所在目录的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 确保 ID 文件始终在 daily_paper_bot 目录下，而不是运行目录
HISTORY_FILE = os.path.join(BASE_DIR, "processed_ids.txt")
MAX_TEXT_LENGTH = 15000  # 限制传给 LLM 的字符数（防止 token 溢出，约 3-5k tokens）

# 如果使用其他模型（如 DeepSeek, Kimi），请修改 BASE_URL 和 API_KEY
LLM_CLIENT = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
)
# 优先使用环境变量，默认为 reasoner
# LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-reasoner")
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")

def normalize_id(paper_id):
    """
    标准化论文 ID，去除版本号后缀 (如 2402.12345v1 -> 2402.12345)
    """
    if not paper_id:
        return ""
    # 使用正则去掉末尾的 v+数字
    return re.sub(r'v\d+$', '', paper_id.strip())

def load_processed_ids():
    """加载已处理过的论文 ID (自动标准化)"""
    if not os.path.exists(HISTORY_FILE):
        return set()
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        # 读取时标准化，确保旧数据也能被正确去重
        return set(normalize_id(line.strip()) for line in f if line.strip())

def save_processed_id(paper_id):
    """追加保存已处理的论文 ID (保存标准化后的 ID)"""
    norm_id = normalize_id(paper_id)
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{norm_id}\n")

def get_recent_papers(url):
    """
    直接从网页抓取论文列表（ID, 标题, 作者, PDF链接）
    绕过 API 延迟问题
    """
    # 构造准确的 URL 参数：从 0 开始，显示 2000 条
    if "?" in url:
        # 如果已有参数，确保包含 skip=0&show=2000
        # 简单处理：直接替换或追加可能比较复杂，这里假设传入的是基础 URL
        pass
    else:
        url += "?skip=0&show=2000"
    
    print(f"正在访问网页: {url}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    papers = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Arxiv 列表页结构：每天一个 <h3> 日期标题，下面跟着一个 <dl> 列表
        # 我们需要抓取页面上所有的 <dl> 标签
        dls = soup.find_all('dl')
        if not dls:
            print("未找到论文列表结构 (dl 标签)")
            return []
            
        all_dts = []
        all_dds = []
        
        for dl in dls:
            all_dts.extend(dl.find_all('dt'))
            all_dds.extend(dl.find_all('dd'))
        
        print(f"网页上发现了 {len(all_dts)} 篇论文。")
        
        for dt, dd in zip(all_dts, all_dds):
            # 1. 提取 ID 和 PDF 链接
            # <a title="Abstract" href="/abs/2402.xxxxx">arXiv:2402.xxxxx</a>
            a_abs = dt.find('a', title='Abstract')
            if not a_abs:
                continue
                
            raw_id = a_abs.text.strip().replace('arXiv:', '')
            paper_url = f"https://arxiv.org{a_abs['href']}"
            
            # 提取 PDF 链接
            # 通常在 dt 里有个 <a title="Download PDF" href="/pdf/2402.xxxxx">pdf</a>
            a_pdf = dt.find('a', title='Download PDF')
            if a_pdf:
                pdf_url = f"https://arxiv.org{a_pdf['href']}"
            else:
                pdf_url = paper_url.replace('/abs/', '/pdf/')
            
            # 2. 提取标题
            # <div class="list-title mathjax">Title: <span class="descriptor">Title:</span> Actual Title</div>
            title_div = dd.find('div', class_='list-title')
            if title_div:
                # 去掉 "Title:" 前缀
                title = title_div.text.replace('Title:', '', 1).strip()
            else:
                title = "Unknown Title"
                
            # 3. 提取作者
            # <div class="list-authors">Authors: <a href="...">Name</a>, ...</div>
            authors_div = dd.find('div', class_='list-authors')
            if authors_div:
                authors = authors_div.text.replace('Authors:', '', 1).strip().split('\n')[0]
            else:
                authors = "Unknown Authors"
                
            papers.append({
                "id": raw_id,
                "title": title,
                "authors": authors,
                "url": paper_url,
                "pdf_url": pdf_url
            })
            
        return papers
    except Exception as e:
        print(f"网页抓取失败: {e}")
        return []

def download_and_parse_pdf(paper_info):
    """
    直接通过 URL 下载 PDF 并解析
    """
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR)
        
    paper_id = paper_info['id']
    pdf_url = paper_info['pdf_url']
    # 确保 URL 是 .pdf 结尾
    if not pdf_url.endswith('.pdf'):
        pdf_url += ".pdf"
        
    pdf_path = os.path.join(PDF_DIR, f"{paper_id}.pdf")
    
    # 1. 下载
    if not os.path.exists(pdf_path):
        print(f"正在下载 PDF: {pdf_url} ...")
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(pdf_url, headers=headers, timeout=30)
            if response.status_code == 200:
                with open(pdf_path, 'wb') as f:
                    f.write(response.content)
                time.sleep(1)
            else:
                print(f"下载失败，状态码: {response.status_code}")
                return ""
        except Exception as e:
            print(f"下载异常: {e}")
            return ""
    else:
        print(f"PDF 已存在: {pdf_path}")

    # 2. 解析
    print(f"正在解析 PDF 内容...")
    try:
        text_content = ""
        reader = pypdf.PdfReader(pdf_path)
        for page in reader.pages:
            extract = page.extract_text()
            if extract:
                text_content += extract + "\n"
        
        if not text_content.strip():
            print("警告: PDF 解析结果为空（可能是扫描版）")
            
        return text_content
    except Exception as e:
        print(f"解析 PDF 失败: {e}")
        return ""

def summarize_paper_full_text(paper_info, full_text):
    """
    调用 LLM 对论文全文进行总结 (返回 JSON 结构)
    """
    print(f"正在根据全文总结: {paper_info['title']}...")
    
    if not full_text:
        return {"summary_md": "无法获取全文内容，跳过总结。", "category": "Unknown", "keywords": []}

    truncated_text = full_text[:MAX_TEXT_LENGTH]
    
    prompt = f"""
    请你作为一个专业的 AI 领域研究员，详细阅读以下论文（已截取前部分），提取关键信息。
    
    论文标题: {paper_info['title']}
    
    论文内容片段:
    {truncated_text}
    ... (内容过长已截断)
    
    请严格按照以下 JSON 格式输出（不要包含 Markdown 代码块标记，只返回纯 JSON 字符串）：
    {{
        "summary_md": "这里放 Markdown 格式的详细总结，包含核心痛点、方法创新、实验结果、一句话评价等章节...",
        "category": "论文所属的具体细分领域，例如 'Text-to-Speech', 'Speech Recognition', 'Audio Enhancement'",
        "keywords": ["关键词1", "关键词2", "关键词3"],
        "related_works": ["提到的相关论文或基线方法名称1", "方法2"]
    }}
    """
    
    try:
        response = LLM_CLIENT.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "你是一个专业的学术论文助手。必须返回合法的 JSON 格式。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"总结失败: {e}")
        return {
            "summary_md": f"总结生成失败: {e}",
            "category": "Error",
            "keywords": [],
            "related_works": []
        }

def generate_report(processed_papers):
    """
    生成 Markdown 和 HTML 报告
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # --- 1. 生成 Markdown ---
    md_filename = os.path.join(OUTPUT_DIR, f"Arxiv_Report_{date_str}.md")
    md_content = f"# Arxiv Daily Deep Report - {date_str}\n\n"
    md_content += f"**来源**: {ARXIV_URL}\n"
    md_content += f"**篇数**: {len(processed_papers)}\n"
    md_content += "---\n\n"
    
    for i, p in enumerate(processed_papers, 1):
        md_content += f"## {i}. {p['title']}\n\n"
        md_content += f"**作者**: {p['authors']}\n"
        md_content += f"**链接**: [{p['id']}]({p['url']})\n"
        md_content += f"**分类**: {p.get('category', 'N/A')} | **关键词**: {', '.join(p.get('keywords', []))}\n\n"
        md_content += f"{p.get('summary_md', '')}\n\n"
        md_content += "---\n\n"
        
    with open(md_filename, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Markdown 报告已生成: {md_filename}")

    # --- 2. 生成 HTML ---
    html_filename = os.path.join(OUTPUT_DIR, f"Arxiv_Report_{date_str}.html")
    
    html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arxiv Daily Report - {date}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f7fa;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #eaeaea;
        }}
        .header h1 {{ margin-bottom: 10px; color: #2c3e50; }}
        .meta {{ color: #7f8c8d; font-size: 0.9em; }}
        
        .paper-card {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            padding: 25px;
            transition: transform 0.2s;
        }}
        .paper-card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0,0,0,0.15); }}
        
        .paper-title {{ 
            margin-top: 0; 
            color: #2c3e50; 
            font-size: 1.4em;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }}
        .paper-title a {{ text-decoration: none; color: inherit; }}
        .paper-title a:hover {{ color: #3498db; }}
        
        .paper-meta {{
            font-size: 0.85em;
            color: #666;
            margin-bottom: 20px;
            background: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
        }}
        
        .summary-section {{ margin-top: 15px; }}
        .summary-section h3 {{ 
            font-size: 1.1em; 
            color: #34495e; 
            margin-top: 20px; 
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }}
        
        .tag {{
            display: inline-block;
            background: #e1ecf4;
            color: #39739d;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 5px;
        }}
        .category-tag {{
            background: #e8f6f3;
            color: #1abc9c;
            border: 1px solid #a3e4d7;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Arxiv Daily Deep Report</h1>
        <div class="meta">
            日期: {date} | 来源: eess.AS | 新增论文: {count} 篇
        </div>
    </div>
    
    {content}
    
    <div style="text-align: center; color: #999; font-size: 0.8em; margin-top: 50px;">
        Generated by AI Daily Bot
    </div>
</body>
</html>
    """
    
    cards_html = ""
    for p in processed_papers:
        summary_md = p.get('summary_md', '') or p.get('summary', '') 
        summary_html = markdown.markdown(summary_md)
        category = p.get('category', 'Unknown')
        keywords = p.get('keywords', [])
        
        keywords_html = "".join([f'<span class="tag">{k}</span>' for k in keywords])
        
        cards_html += f"""
        <div class="paper-card">
            <h2 class="paper-title">
                <a href="{p['url']}" target="_blank">{p['title']}</a>
            </h2>
            <div class="paper-meta">
                <span class="tag category-tag">{category}</span>
                <strong>ID:</strong> <span class="tag">{p['id']}</span>
                <a href="pdfs/{p['id']}.pdf" target="_blank" class="tag" style="background:#e74c3c; color:white; text-decoration:none;">📄 Local PDF</a><br>
                <strong>Authors:</strong> {p['authors']}<br>
                <div style="margin-top:5px">{keywords_html}</div>
            </div>
            <div class="summary-section">
                {summary_html}
            </div>
        </div>
        """
        
    final_html = html_template.format(
        date=date_str,
        count=len(processed_papers),
        content=cards_html
    )
    
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"HTML 网页报告已生成: {html_filename}")
    return html_filename

def main():
    # 1. 直接从网页获取论文列表（跳过 API）
    all_papers = get_recent_papers(ARXIV_URL)
    
    # 加载历史记录并过滤
    processed_ids = load_processed_ids()
    # 过滤时使用 normalize_id
    new_papers = [p for p in all_papers if normalize_id(p['id']) not in processed_ids]
    
    print(f"共扫描到 {len(all_papers)} 篇论文，其中 {len(new_papers)} 篇未处理。")
    
    if not new_papers:
        print("没有新论文需要处理。")
        return

    # 演示模式：限制处理数量（生产环境请注释掉）
    # new_papers = new_papers[:3] 

    processed_papers = []
    
    # 2. 逐个处理：下载 -> 解析 -> 总结
    for paper_info in new_papers:
        paper_id = paper_info['id']
        norm_id = normalize_id(paper_id) # 获取基础 ID
        
        if norm_id in processed_ids:
            continue
            
        # 下载并解析全文
        full_text = download_and_parse_pdf(paper_info)
        
        # 生成总结
        summary_data = summarize_paper_full_text(paper_info, full_text)
        
        # 合并结果
        paper_info.update(summary_data)
        processed_papers.append(paper_info)
        
        # 立即记录已处理 ID (标准化后)
        save_processed_id(paper_id)
        processed_ids.add(norm_id)
        
        # 实时更新报告
        print(f"实时更新报告... (当前已处理 {len(processed_papers)} 篇)")
        generate_report(processed_papers)
        
        # --- 新增：实时更新总首页 ---
        try:
            print("实时更新总归档页面...")
            merge_reports.main() 
        except Exception as e:
            print(f"归档更新失败: {e}")
        
    print("所有任务处理完成。")

if __name__ == "__main__":
    main()
