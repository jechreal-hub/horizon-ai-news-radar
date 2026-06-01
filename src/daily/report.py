from datetime import date
from pathlib import Path
from jinja2 import Template
from src.fetchers.base import Article
from src.llm.classifier import CATEGORIES, classify_by_keywords
from loguru import logger


REPORT_DIR = Path("data/reports")

DAILY_TEMPLATE = Template("""# 🪐 Horizon AI 日报 — {{ date }}

> 今日抓取 {{ total_count }} 篇，精选 {{ selected_count }} 篇

{% for cat, items in grouped.items() %}
## {{ cat }}
{% for a in items %}
- [{{ a.title }}]({{ a.url }}) — {{ a.summary }} ⭐{{ a.importance }}
{% endfor %}

{% endfor %}
---
*由 Horizon AI 新闻雷达自动生成 | {{ now }}*
""")

class DailyReport:
    def generate(self, articles: list[Article]) -> str:
        grouped = {cat: [] for cat in CATEGORIES}
        for a in articles:
            if a.importance >= 3:
                cat = classify_by_keywords(a.title, a.tags)
                grouped[cat].append(a)
        selected = sum(len(v) for v in grouped.values())
        today = date.today().isoformat()
        return DAILY_TEMPLATE.render(
            date=today,
            now=today,
            total_count=len(articles),
            selected_count=selected,
            grouped={k: v for k, v in grouped.items() if v},
        )

    def save(self, content: str):
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        today = date.today().isoformat()
        path = REPORT_DIR / f"{today}.md"
        path.write_text(content, encoding="utf-8")
        logger.info(f"Daily report saved to {path}")
