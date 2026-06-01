from bs4 import BeautifulSoup
import re


def strip_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_content(raw: str) -> str:
    text = strip_html(raw)
    return normalize_whitespace(text)
