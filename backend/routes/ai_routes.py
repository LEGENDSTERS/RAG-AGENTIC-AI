
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.agents.router import router_agent


print("AI_ROUTES_LOADED")

router = APIRouter()

OLLAMA_MODEL = "phi3:mini"



class QuestionRequest(BaseModel):
    question: str





@router.get("/test")
def test():
    print("TEST ENDPOINT HIT")
    return {"message": "working"}



@router.post("/ask")
def ask_question(payload: QuestionRequest):

    question = payload.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    return router_agent(question)