from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from nodes.summarize_passage import summarize_passage
from nodes.extract_keywords import extract_keywords


class WorkflowState(TypedDict):
    query: str
    summary: str
    keywords: List[str]


def build_graph():
    """
    Constructs a sequential LangGraph workflow:
    query → summarize → extract_keywords
    """
    graph = StateGraph(WorkflowState)

    # Define nodes
    graph.add_node("Summarize_Passage", summarize_passage)
    graph.add_node("Extract_Keywords", extract_keywords)

    # Define edges
    graph.add_edge(START, "Summarize_Passage")
    graph.add_edge("Summarize_Passage", "Extract_Keywords")
    graph.add_edge("Extract_Keywords", END)

    return graph.compile()
