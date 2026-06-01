from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Article:
    title: str
    url: str
    source: str
    published_at: datetime | None = None
    raw_content: str = ""
    summary: str = ""
    tags: list[str] = field(default_factory=list)
    importance: int = 3


class BaseFetcher(ABC):
    @abstractmethod
    async def fetch(self) -> list[Article]:
        ...

    @property
    @abstractmethod
    def source_name(self) -> str:
        ...
