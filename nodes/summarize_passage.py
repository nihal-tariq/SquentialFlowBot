from typing import Dict
from models.gemini_client import get_gemini_model
from prompts import SUMMARY_PROMPT

model = get_gemini_model()


def summarize_passage(state: Dict) -> Dict:
    """
    Summarizes the given passage while preserving tone, meaning, and factual accuracy.
    """
    passage = state["query"]
    prompt = SUMMARY_PROMPT.format(text=passage)

    response = model.invoke(prompt)
    summary = response.content.strip()

    state["summary"] = summary
    return state
