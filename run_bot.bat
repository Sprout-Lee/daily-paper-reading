@echo off
REM 激活 Conda 环境
call conda activate cp311_np2_torch

REM 检查是否激活成功
if %errorlevel% neq 0 (
    echo 激活环境失败，请检查 conda 是否在 PATH 中，或者环境名称是否正确。
    pause
    exit /b %errorlevel%
)

REM 运行 Python 脚本
echo 正在运行 Daily Paper Bot...
python daily_paper_bot/main.py

REM 如果脚本执行出错，暂停以便查看日志
if %errorlevel% neq 0 (
    echo 运行出错！
    pause
) else (
    echo 运行完成。
)

