import json
from openai import AsyncOpenAI
from src.config import settings
from src.fetchers.base import Article
from loguru import logger


SYSTEM_PROMPT = """你是一个 AI 行业新闻编辑。
对每篇文章生成：
1. 一句话中文摘要 (50字内)
2. 3 个标签
3. 重要性评分 1-5
输出 JSON 格式: {"summary": "...", "tags": [...], "importance": N}"""


class LLMSummarizer:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url,
        )

    async def summarize(self, article: Article) -> dict:
        try:
            resp = await self.client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Title: {article.title}\n\n{article.raw_content[:2000]}"},
                ],
            )
            content = resp.choices[0].message.content
            if not content:
                return {"summary": "", "tags": [], "importance": 3}
            content = content.strip()
            if content.startswith("```"):
                content = content.split("\n", 1)[-1]
                content = content.rsplit("```", 1)[0]
            return json.loads(content)
        except (json.JSONDecodeError, Exception) as e:
            logger.warning(f"LLM parse failed for {article.title}: {e}")
            return {"summary": str(content)[:100] if "content" in dir() else "", "tags": [], "importance": 3}
