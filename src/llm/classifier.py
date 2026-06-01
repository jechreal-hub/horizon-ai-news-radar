CATEGORIES = [
    "重磅发布",     # Major releases
    "行业动态",     # Industry news
    "工具 & 开源",  # Tools & OSS
    "融资 & 商业",  # Funding & Business
    "研究 & 论文",  # Research & Papers
]


def classify_by_keywords(title: str, tags: list[str]) -> str:
    title_lower = title.lower()
    text = title_lower + " " + " ".join(tags).lower()
    if any(kw in text for kw in ["release", "launch", "announce", "发布", "announcing"]):
        return "重磅发布"
    if any(kw in text for kw in ["funding", "融资", "acquisition", "收购", "商业"]):
        return "融资 & 商业"
    if any(kw in text for kw in ["open source", "github", "开源", "tool", "library"]):
        return "工具 & 开源"
    if any(kw in text for kw in ["paper", "research", "study", "研究", "arxiv"]):
        return "研究 & 论文"
    return "行业动态"
