

from fastapi import FastAPI
from backend.routes.ai_routes import router as ai_router
app = FastAPI(
    title="Insurance Policy RAG API",
    description="Ask questions about the insurance policy using RAG + Ollama.",
    version="1.0.0",
)

app.include_router(ai_router, prefix="/api", tags=["RAG"])


@app.get("/")
def root():
    return {
        "message": "Insurance RAG API is running.",
        "usage": "POST /api/ask  with JSON body: { 'question': 'your question here' }",
        "docs": "/docs",
    }
