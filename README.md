# 🪐 Horizon AI 新闻雷达

> 定时抓取行业 AI 资讯 → LLM 智能摘要 → 推送微信 → 生成日报

## 快速开始

```bash
# 1. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API Key

# 2. 安装依赖
uv sync

# 3. 运行
uv run python -m src.main fetch    # 只抓取
uv run python -m src.main run      # 完整流水线
uv run python -m src.main schedule # 定时调度
```

## 结构

```
src/
  fetchers/    # 数据源采集
  cleaners/    # 清洗管道
  llm/         # LLM 摘要/分类
  pushers/     # 推送通道
  daily/       # 日报生成
  storage/     # 数据存储
  scheduler.py # 定时调度
  config.py    # 配置管理
  main.py      # CLI 入口
```

## 技术栈

- Python 3.12+ / uv
- aiohttp / feedparser / BeautifulSoup
- OpenAI SDK / pydantic-settings
- APScheduler / SQLAlchemy + aiosqlite
- Jinja2 / loguru
