import os
import sys
import json
import arxiv
from openai import OpenAI
from dotenv import load_dotenv
import pypdf

# 复用 main.py 中的部分逻辑 (为了独立性这里简单复制，也可以 import)
load_dotenv()
LLM_CLIENT = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
)
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")

def extract_references_with_llm(pdf_text):
    """让 LLM 分析出最重要的参考文献"""
    print("正在分析核心参考文献...")
    prompt = f"""
    请阅读以下论文内容，提取出对理解该论文最关键的 3-5 篇参考文献（Background / Baseline）。
    
    论文内容片段:
    {pdf_text[:10000]}
    
    请只返回参考文献的标题列表，JSON 格式：
    {{ "references": ["Title 1", "Title 2", ...] }}
    """
    
    try:
        response = LLM_CLIENT.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content).get("references", [])
    except Exception as e:
        print(f"分析引用失败: {e}")
        return []

def search_and_download(title):
    """在 Arxiv 上搜索标题并下载"""
    print(f"正在搜索: {title}...")
    client = arxiv.Client()
    search = arxiv.Search(query=f'ti:"{title}"', max_results=1)
    
    try:
        result = next(client.results(search))
        print(f"找到: {result.title} ({result.entry_id})")
        
        pdf_name = result.entry_id.split('/')[-1] + ".pdf"
        pdf_path = os.path.join("pdfs", "references", pdf_name)
        
        if not os.path.exists("pdfs/references"):
            os.makedirs("pdfs/references")
            
        if not os.path.exists(pdf_path):
            result.download_pdf(dirpath="pdfs/references", filename=pdf_name)
            print("下载完成。")
        else:
            print("文件已存在。")
            
        return pdf_path, result
    except StopIteration:
        print("未找到对应论文。")
        return None, None
    except Exception as e:
        print(f"搜索出错: {e}")
        return None, None

def main():
    if len(sys.argv) < 2:
        print("用法: python citation_miner.py <pdf_path>")
        return
        
    pdf_path = sys.argv[1]
    
    # 1. 读取原文
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = "".join([p.extract_text() for p in reader.pages[:5]]) # 只读前5页通常包含Intro
    except:
        print("读取 PDF 失败")
        return

    # 2. 提取引用
    refs = extract_references_with_llm(text)
    print(f"识别到 {len(refs)} 篇核心引用。")
    
    # 3. 搜索并下载
    for title in refs:
        path, res = search_and_download(title)
        # 这里你可以继续接上 summarize 的逻辑
        if path:
            print(f"已获取背景论文: {path}")

if __name__ == "__main__":
    main()

