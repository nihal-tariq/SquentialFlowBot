from fastapi import FastAPI, HTTPException, Form, Query
from pydantic import BaseModel, Field
from typing import List
from graph_builder import build_graph

app = FastAPI(title="LangGraph Sequential Workflow API")

# Build the LangGraph workflow once at startup
graph = build_graph()


# -----------------------------
# Response Model
# -----------------------------
class WorkflowResponse(BaseModel):
    """Schema for workflow output."""
    summary: str = Field(..., description="Generated summary of the input passage.")
    keywords: List[str] = Field(..., description="Extracted keywords from the passage.")


# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/process", response_model=WorkflowResponse, summary="Process Passage")
async def process_passage(
    passage: str = Form(..., description="The input passage to be processed.")
):
    """
    Takes a passage as input (as form data or query parameter)
    and returns its summary and extracted keywords.
    """
    try:
        # Prepare initial state for LangGraph
        state = {
            "query": passage,
            "summary": "",
            "keywords": [],
        }

        # Invoke the LangGraph workflow
        result = graph.invoke(state)

        # Ensure expected keys exist in the result
        if not all(k in result for k in ["summary", "keywords"]):
            raise ValueError("Incomplete result returned from workflow.")

        # Return structured response
        return WorkflowResponse(
            summary=result["summary"],
            keywords=result["keywords"],
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {e}")
