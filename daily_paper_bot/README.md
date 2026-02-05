# Arxiv Daily Paper Bot

这个工具每天自动抓取指定 Arxiv 页面（如 eess.AS）的最新论文，使用 AI 生成中文摘要，并保存为 Markdown 报告。

## 目录结构

- `main.py`: 主程序，负责抓取、总结和生成报告。
- `requirements.txt`: Python 依赖库列表。
- `env_example.txt`: 环境变量配置文件示例。
- `reports/`: 生成的日报将保存在这里。

## 快速开始

### 1. 安装依赖

确保你已经安装了 Python (建议 3.8+)。在终端运行：

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

1. 在当前目录下创建一个名为 `.env` 的文件。
2. 将 `env_example.txt` 的内容复制进去。
3. 填入你的 LLM API Key（支持 OpenAI, DeepSeek, Kimi 等兼容 OpenAI SDK 的模型）。

示例 `.env`:
```ini
LLM_API_KEY=sk-your-api-key-here
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-3.5-turbo
```

### 3. 运行程序

直接运行 Python 脚本：

```bash
python main.py
```

程序将：
1. 访问 `https://arxiv.org/list/eess.AS/recent`。
2. 获取最新论文的 ID 和详细摘要。
3. 调用 AI 进行总结。
4. 在 `reports/` 目录下生成 `Arxiv_Daily_Report_YYYY-MM-DD.md`。

## 如何实现每天自动运行？

### 方法一：GitHub Actions (推荐，免费且无需本地开机)

1. 将此项目上传到 GitHub 仓库。
2. 在仓库设置 (Settings) -> Secrets and variables -> Actions 中添加 `LLM_API_KEY`。
3. 创建 `.github/workflows/daily_run.yml` 文件：

```yaml
name: Daily Paper Bot
on:
  schedule:
    - cron: '0 0 * * *' # 每天 UTC 时间 0点 (北京时间 8点) 运行
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
        run: pip install -r requirements.txt
      - name: Run bot
        env:
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
          LLM_BASE_URL: "https://api.openai.com/v1" # 根据需要修改
          LLM_MODEL: "gpt-3.5-turbo"
        run: python main.py
      - name: Commit and push report
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add reports/
          git commit -m "Add daily report"
          git push
```

### 方法二：本地 Windows 计划任务

1. 打开“任务计划程序” (Task Scheduler)。
2. 创建基本任务 -> 设置每天触发。
3. 操作 -> 启动程序 -> 选择 `python.exe` 路径，参数填 `main.py` 的完整路径。

## 自定义

- **修改抓取源**: 在 `main.py` 中修改 `ARXIV_URL` 变量。
- **修改总结风格**: 在 `main.py` 的 `summarize_paper` 函数中修改 `prompt`。

