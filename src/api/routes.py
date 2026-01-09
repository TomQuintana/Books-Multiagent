from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..llm.ia_service import ia_service

router = APIRouter()


class QueryRequest(BaseModel):
    message: str


class QueryResponse(BaseModel):
    response: str


@router.get("/")
async def root():
    return {"message": "Welcome to ASTA API - Book Management System"}


@router.get("/ask")
async def ask_agent(question: str):
    """
    GET endpoint that processes a question using the AI agent with book tools.

    Args:
        question: The question to ask the AI agent

    Returns:
        A JSON response with the agent's answer after using available tools

    Example:
        GET /ask?question=Lista todos los libros
    """
    try:
        response = ia_service.process_query(question)
        return {"question": question, "answer": response}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing request: {str(e)}"
        )


@router.post("/query")
async def process_query(request: QueryRequest) -> QueryResponse:
    """
    POST endpoint that processes a query using the AI agent with book tools.

    Args:
        request: QueryRequest with the user's message

    Returns:
        QueryResponse with the agent's response

    Example:
        POST /query
        Body: {"message": "Crea un libro llamado '1984' escrito por George Orwell"}
    """
    try:
        response = ia_service.process_query(request.message)
        return QueryResponse(response=response)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing request: {str(e)}"
        )
