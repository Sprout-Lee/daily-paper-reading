import os
import re
import markdown
from datetime import datetime

import shutil # 新增

REPORTS_DIR = "reports"
OUTPUT_FILE = "reports/All_Papers_Archive.html"
INDEX_FILE = "index.html"  # 网站首页文件

def parse_md_file(filepath):
    """
    解析单个 MD 文件，提取论文信息
    假设格式相对固定：
    # Arxiv Daily Deep Report - YYYY-MM-DD
    ...
    ## 1. Title
    **作者**: ...
    **链接**: ...
    **分类**: ... | **关键词**: ...
    Summary content...
    ---
    """
    filename = os.path.basename(filepath)
    # 从文件名提取日期 (Arxiv_Report_2024-02-05.md)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    date = date_match.group(1) if date_match else "Unknown Date"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 改进的分割逻辑：先按 "## Number. " 分割，因为这比 --- 更唯一
    # 但由于 split 会移除分隔符，我们需要用 lookahead 或者手动处理
    # 这里采用逐行扫描的状态机模式，比正则 split 更稳健
    
    lines = content.split('\n')
    current_paper = {}
    papers = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # 1. 检测新论文开始：## 数字. 标题
        title_match = re.match(r'^##\s+\d+\.\s+(.+)', line)
        if title_match:
            # 如果当前已经有正在处理的论文，保存它
            if current_paper:
                # 提取总结内容：从 header_end_idx 到当前行之前
                if 'header_end_idx' in current_paper:
                    start = current_paper['header_end_idx']
                    # 去掉末尾可能的 ---
                    summary_lines = lines[start:i]
                    # 过滤掉末尾的空行和分隔线
                    while summary_lines and (not summary_lines[-1].strip() or summary_lines[-1].strip() == '---'):
                        summary_lines.pop()
                    current_paper['summary_md'] = "\n".join(summary_lines).strip()
                
                papers.append(current_paper)
            
            # 开始新论文
            current_paper = {
                "date": date,
                "title": title_match.group(1).strip(),
                "authors": "Unknown",
                "id": "",
                "url": "",
                "category": "Unknown",
                "keywords": [],
                "summary_md": "",
                "header_end_idx": i + 1 # 暂定内容从下一行开始
            }
            continue
            
        # 2. 提取元数据 (仅在当前有论文上下文时)
        if current_paper:
            # 作者
            if line.startswith("**作者**:"):
                current_paper['authors'] = line.replace("**作者**:", "").strip()
                current_paper['header_end_idx'] = i + 1
            # 链接
            elif line.startswith("**链接**:"):
                link_match = re.search(r'\[(.*?)\]\((.*?)\)', line)
                if link_match:
                    current_paper['id'] = link_match.group(1)
                    current_paper['url'] = link_match.group(2)
                current_paper['header_end_idx'] = i + 1
            # 分类和关键词
            elif "**分类**:" in line:
                cat_part = line.split("|")[0] if "|" in line else line
                key_part = line.split("|")[1] if "|" in line else ""
                
                current_paper['category'] = cat_part.replace("**分类**:", "").strip()
                if "**关键词**:" in key_part:
                    keys = key_part.replace("**关键词**:", "").strip()
                    current_paper['keywords'] = [k.strip() for k in keys.split(',')]
                current_paper['header_end_idx'] = i + 1

    # 循环结束，保存最后一篇
    if current_paper:
        if 'header_end_idx' in current_paper:
            start = current_paper['header_end_idx']
            summary_lines = lines[start:]
            while summary_lines and (not summary_lines[-1].strip() or summary_lines[-1].strip() == '---'):
                summary_lines.pop()
            current_paper['summary_md'] = "\n".join(summary_lines).strip()
        papers.append(current_paper)
        
    return papers

def generate_archive_html(all_papers):
    """
    生成汇总 HTML
    """
    # 按日期倒序排序，如果日期相同则按 ID 倒序（确保最新的绝对在前面）
    all_papers.sort(key=lambda x: (x['date'], x['id']), reverse=True)
    
    html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arxiv Papers Archive</title>
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
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #eaeaea;
        }}
        .header h1 {{ margin-bottom: 10px; color: #2c3e50; }}
        .stats {{ color: #7f8c8d; font-size: 0.9em; margin-top: 10px; }}
        
        .date-divider {{
            margin: 40px 0 20px 0;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
            color: #2c3e50;
            font-size: 1.5em;
        }}
        
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
        .summary-section p {{ margin-bottom: 10px; }}
        .summary-section ul {{ padding-left: 20px; }}
        
        .tag {{
            display: inline-block;
            background: #e1ecf4;
            color: #39739d;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        .category-tag {{
            background: #e8f6f3;
            color: #1abc9c;
            border: 1px solid #a3e4d7;
        }}
        .date-tag {{
            background: #fef9e7;
            color: #f1c40f;
            border: 1px solid #f9e79f;
            float: right;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Arxiv Papers Knowledge Base</h1>
        <div class="stats">
            共收录 {total_papers} 篇论文 | 涵盖 {total_days} 天的数据
        </div>
    </div>
    
    {content}
    
    <div style="text-align: center; color: #999; font-size: 0.8em; margin-top: 50px;">
        Generated by AI Daily Bot
    </div>
</body>
</html>
    """
    
    content_html = ""
    current_date = None
    
    for p in all_papers:
        # 添加日期分隔符
        if p['date'] != current_date:
            current_date = p['date']
            content_html += f'<h2 class="date-divider">📅 {current_date}</h2>'
            
        summary_html = markdown.markdown(p['summary_md'])
        keywords_html = "".join([f'<span class="tag">{k}</span>' for k in p['keywords']])
        
        content_html += f"""
        <div class="paper-card">
            <h2 class="paper-title">
                <a href="{p['url']}" target="_blank">{p['title']}</a>
                <span style="float:right; font-size:0.6em; color:#999; font-weight:normal;">{p['date']}</span>
            </h2>
            <div class="paper-meta">
                <span class="tag category-tag">{p['category']}</span>
                <strong>ID:</strong> <span class="tag">{p['id']}</span><br>
                <strong>Authors:</strong> {p['authors']}<br>
                <div style="margin-top:5px">{keywords_html}</div>
            </div>
            <div class="summary-section">
                {summary_html}
            </div>
        </div>
        """
    
    unique_days = len(set(p['date'] for p in all_papers))
    final_html = html_template.format(
        total_papers=len(all_papers),
        total_days=unique_days,
        content=content_html
    )
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"汇总报告已生成: {OUTPUT_FILE}")
    
    # --- 新增：复制为 index.html ---
    shutil.copy(OUTPUT_FILE, INDEX_FILE)
    print(f"已更新网站首页: {INDEX_FILE}")

def main():
    if not os.path.exists(REPORTS_DIR):
        print(f"目录 {REPORTS_DIR} 不存在。")
        return
        
    all_papers = []
    files = [f for f in os.listdir(REPORTS_DIR) if f.endswith('.md') and f.startswith('Arxiv_')]
    
    print(f"找到 {len(files)} 个历史报告文件。")
    
    for f in files:
        path = os.path.join(REPORTS_DIR, f)
        print(f"正在解析: {f}...")
        try:
            papers = parse_md_file(path)
            all_papers.extend(papers)
        except Exception as e:
            print(f"解析 {f} 失败: {e}")
            
    if all_papers:
        generate_archive_html(all_papers)
    else:
        print("没有找到任何论文数据。")

if __name__ == "__main__":
    main()

