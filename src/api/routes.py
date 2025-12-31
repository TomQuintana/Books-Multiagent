from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..llm.client import llm

router = APIRouter()


class QueryRequest(BaseModel):
    message: str


class QueryResponse(BaseModel):
    response: str


@router.get("/")
async def root():
    return {"message": "Welcome to ASTA API"}


@router.get("/ask")
async def ask_llm(question: str):
    """
    Simple GET endpoint that sends a question to the LLM and returns the response.

    Args:
        question: The question to ask the LLM

    Returns:
        A JSON response with the LLM's answer
    """
    try:
        response = llm.invoke(question)
        return {
            "question": question,
            "answer": response.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
