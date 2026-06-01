import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from .base import BaseFetcher, Article


class WebFetcher(BaseFetcher):
    def __init__(self, name: str, url: str, parser: str = "html.parser"):
        self._name = name
        self._url = url
        self._parser = parser

    @property
    def source_name(self) -> str:
        return self._name

    async def fetch(self) -> list[Article]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url, timeout=30) as resp:
                html = await resp.text()
        soup = BeautifulSoup(html, self._parser)
        # Generic extraction; override in subclasses for specific sites
        items = []
        for item in soup.select("article, .post, .entry, li")[:20]:
            title_el = item.find(["h1", "h2", "h3", "a"])
            if not title_el:
                continue
            link = title_el.get("href", "") if title_el.name == "a" else ""
            if link and not link.startswith("http"):
                link = self._url.rstrip("/") + "/" + link.lstrip("/")
            items.append(Article(
                title=title_el.get_text(strip=True),
                url=link,
                source=self._name,
                published_at=datetime.now(timezone.utc),
                raw_content=item.get_text(strip=True),
            ))
        return items
