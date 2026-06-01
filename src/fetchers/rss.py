import feedparser
from datetime import datetime, timezone
from .base import BaseFetcher, Article


class RSSFetcher(BaseFetcher):
    def __init__(self, name: str, url: str):
        self._name = name
        self._url = url

    @property
    def source_name(self) -> str:
        return self._name

    async def fetch(self) -> list[Article]:
        feed = feedparser.parse(self._url)
        articles = []
        for entry in feed.entries[:20]:
            published = None
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            articles.append(Article(
                title=entry.get("title", ""),
                url=entry.get("link", ""),
                source=self._name,
                published_at=published,
                raw_content=entry.get("summary", ""),
            ))
        return articles
