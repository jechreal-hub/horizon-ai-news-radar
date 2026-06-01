from src.fetchers.base import Article


class DedupPipeline:
    def __init__(self):
        self._seen_urls: set[str] = set()
        self._seen_titles: set[str] = set()

    def is_duplicate(self, article: Article) -> bool:
        # URL dedup
        if article.url and article.url in self._seen_urls:
            return True
        # Title fuzzy dedup (simple: normalize & compare)
        norm_title = article.title.strip().lower()
        if norm_title and norm_title in self._seen_titles:
            return True
        self._seen_urls.add(article.url)
        self._seen_titles.add(norm_title)
        return False

    def reset(self):
        self._seen_urls.clear()
        self._seen_titles.clear()
