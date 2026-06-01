from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # OpenAI / LLM
    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"

    # Push channels
    wecom_webhook_url: Optional[str] = None
    serverchan_send_key: Optional[str] = None
    pushplus_token: Optional[str] = None

    # Behavior
    max_articles_per_fetch: int = 50
    dedup_days: int = 3
    report_retention_days: int = 30

    # Database
    database_url: str = "sqlite+aiosqlite:///data/horizon.db"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
