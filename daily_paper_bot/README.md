# Arxiv Daily Paper Bot

这个工具每天自动抓取多个 Arxiv 页面（cs.SD 和 eess.AS）的最新论文，使用 AI 生成中文摘要，并保存为 Markdown 报告。

## 目录结构

- `main.py`: 主程序，负责抓取、总结和生成报告。
- `requirements.txt`: Python 依赖库列表。
- `.env`: 环境变量配置文件。
- `../reports/YYYY-MM/`: 生成的日报将按月份保存在这里。

## 快速开始

### 1. 安装依赖

确保你已经安装了 Python (建议 3.8+)。在终端运行：

```bash
pip install -r daily_paper_bot/requirements.txt
```

### 2. 配置 API Key

1. 在仓库根目录创建一个名为 `.env` 的文件。
2. 填入你的 LLM API Key（支持 OpenAI, DeepSeek, Kimi 等兼容 OpenAI SDK 的模型）。

示例 `.env`:
```ini
LLM_API_KEY=sk-your-api-key-here
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-3.5-turbo
```

### 3. 运行程序

直接运行 Python 脚本：

```bash
python daily_paper_bot/main.py
```

程序将：
1. 访问 `https://arxiv.org/list/cs.SD/recent` 和 `https://arxiv.org/list/eess.AS/recent`。
2. 获取最新论文的 ID 和详细摘要。
3. 调用 AI 进行总结。
4. 在 `reports/YYYY-MM/` 目录下生成 `Arxiv_Report_YYYY-MM-DD.md` 和对应 HTML。
5. 更新 `reports/All_Papers_Archive.html`、`public/index.html` 和根目录 `index.html`。

## 如何实现每天自动运行？

### 方法一：GitHub Actions (推荐，免费且无需本地开机)

1. 将此项目上传到 GitHub 仓库。
2. 在仓库设置 (Settings) -> Secrets and variables -> Actions 中添加 `LLM_API_KEY`。
3. 使用仓库里的 `.github/workflows/daily_process.yml` 文件：

```yaml
name: Daily Arxiv Bot
on:
  schedule:
    - cron: '0 3 * * *' # 每天 UTC 时间 3点 (北京时间 11点) 运行
  workflow_dispatch: # 允许手动触发

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r daily_paper_bot/requirements.txt
      - name: Run bot
        env:
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
          LLM_BASE_URL: "https://api.openai.com/v1" # 根据需要修改
          LLM_MODEL: "gpt-3.5-turbo"
        run: python daily_paper_bot/main.py
      - name: Commit and push report
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add reports/
          git add public/ index.html daily_paper_bot/processed_ids.txt
          git commit -m "Add daily report"
          git push
```

### 方法二：本地 Windows 计划任务

1. 打开“任务计划程序” (Task Scheduler)。
2. 创建基本任务 -> 设置每天触发。
3. 操作 -> 启动程序 -> 选择 `python.exe` 路径，参数填 `main.py` 的完整路径。

## 自定义

- **修改抓取源**: 在 `main.py` 中修改 `ARXIV_URLS` 列表。
- **修改总结风格**: 在 `main.py` 的 `summarize_paper` 函数中修改 `prompt`。

