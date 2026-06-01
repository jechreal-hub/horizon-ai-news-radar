from abc import ABC, abstractmethod
from src.fetchers.base import Article


class BasePusher(ABC):
    @abstractmethod
    async def push(self, articles: list[Article]) -> bool:
        ...
