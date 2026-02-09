import os
import re
import sys
import pypdf
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 配置
LLM_CLIENT = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
)
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")

def extract_text_from_pdf(pdf_path):
    """提取 PDF 文本并进行简单清洗"""
    print(f"正在读取 PDF: {pdf_path}...")
    try:
        reader = pypdf.PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        return full_text
    except Exception as e:
        print(f"读取 PDF 失败: {e}")
        return ""

def clean_and_split_sentences(text):
    """
    清洗文本并切分为句子
    """
    # 1. 简单的清洗：去掉多余换行，把断行的单词连起来
    text = re.sub(r'-\n', '', text) # hyphenation
    text = re.sub(r'\n', ' ', text) # remove newlines
    text = re.sub(r'\s+', ' ', text) # remove extra spaces
    
    # 2. 分句（简单的正则，不如 nltk 准确但够用）
    # 匹配 . ? ! 后面跟空格和大写字母的情况
    sentences = re.split(r'(?<=[.?!])\s+(?=[A-Z])', text)
    
    # 过滤太短的句子
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    return sentences

def translate_sentences(sentences, batch_size=10):
    """
    批量翻译句子
    """
    translated_pairs = []
    total = len(sentences)
    
    print(f"共提取出 {total} 个句子，开始翻译...")
    
    for i in range(0, total, batch_size):
        batch = sentences[i:i+batch_size]
        print(f"正在翻译第 {i+1}-{min(i+batch_size, total)} 句...")
        
        # 构造 Prompt
        text_block = "\n".join([f"[{j+1}] {s}" for j, s in enumerate(batch)])
        prompt = f"""
        请将以下学术论文的英文句子翻译成中文。
        保持专业术语的准确性。请严格按照原来的编号返回，格式为 "[编号] 中文翻译"。
        
        {text_block}
        """
        
        try:
            response = LLM_CLIENT.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {"role": "system", "content": "你是一个专业的学术翻译助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            result = response.choices[0].message.content
            
            # 解析返回结果
            trans_map = {}
            for line in result.split('\n'):
                match = re.match(r'\[(\d+)\]\s*(.*)', line)
                if match:
                    trans_map[int(match.group(1))] = match.group(2)
            
            # 组合结果
            for j, s in enumerate(batch):
                trans = trans_map.get(j+1, "翻译失败")
                translated_pairs.append((s, trans))
                
            time.sleep(1) # 避免速率限制
            
        except Exception as e:
            print(f"翻译批次失败: {e}")
            for s in batch:
                translated_pairs.append((s, "Error: Translation failed."))
                
    return translated_pairs

def generate_bilingual_html(pairs, title, output_path):
    """生成左右对照 HTML"""
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Deep Read: {title}</title>
    <style>
        body {{ font-family: "Segoe UI", sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .row {{ display: flex; border-bottom: 1px solid #eee; padding: 10px 0; }}
        .row:hover {{ background-color: #f9f9f9; }}
        .en {{ flex: 1; padding-right: 20px; color: #333; }}
        .zh {{ flex: 1; padding-left: 20px; color: #555; border-left: 1px solid #eee; }}
        h1 {{ text-align: center; color: #2c3e50; }}
    </style>
</head>
<body>
    <h1>精读：{title}</h1>
    <div class="container">
"""
    for en, zh in pairs:
        html_content += f"""
        <div class="row">
            <div class="en">{en}</div>
            <div class="zh">{zh}</div>
        </div>
        """
        
    html_content += """
    </div>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"精读报告已生成: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("请提供 PDF 文件路径。用法: python deep_read.py <pdf_path>")
        return
        
    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print("文件不存在")
        return
        
    filename = os.path.basename(pdf_path)
    title = filename.replace('.pdf', '')
    
    # 1. 提取
    text = extract_text_from_pdf(pdf_path)
    if not text: return
    
    # 2. 分句
    sentences = clean_and_split_sentences(text)
    
    # 3. 翻译 (只取前 50 句做演示，防止消耗过多 token，实际使用可去掉切片)
    # sentences = sentences[:50] 
    
    pairs = translate_sentences(sentences)
    
    # 4. 生成 HTML
    output_path = pdf_path.replace('.pdf', '_read.html')
    generate_bilingual_html(pairs, title, output_path)

if __name__ == "__main__":
    main()

