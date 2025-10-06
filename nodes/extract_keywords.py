from typing import Dict
from models.gemini_client import get_gemini_model
from prompts import KEYWORD_EXTRACTION_PROMPT

model = get_gemini_model()


def extract_keywords(
        state: Dict) -> Dict:
    """
    Extracts meaningful, contextually important keywords from the summary.
    """
    summary = state["summary"]
    prompt = KEYWORD_EXTRACTION_PROMPT.format(text=summary)

    response = model.invoke(prompt)
    keywords_text = response.content.strip()

    keywords = [word.strip() for word in keywords_text.split(",") if word.strip()]
    state["keywords"] = keywords
    return state
