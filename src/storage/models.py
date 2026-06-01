from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ArticleModel(Base):
    __tablename__ = "articles"

    id = Column(String, primary_key=True)           # URL hash
    title = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    source = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=True)
    summary = Column(Text, default="")
    tags = Column(String, default="[]")             # JSON array
    importance = Column(Integer, default=3)
    fetched_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class DailyReportModel(Base):
    __tablename__ = "daily_reports"

    date = Column(String, primary_key=True)
    content = Column(Text, default="")
    article_count = Column(Integer, default=0)
    generated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
