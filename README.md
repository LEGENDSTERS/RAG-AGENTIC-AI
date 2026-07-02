Working of the RAG-AGENTIC AI SYSTEM

SINGLE AGENTS:
<img width="930" height="365" alt="Screenshot 2026-07-02 160535" src="https://github.com/user-attachments/assets/7bbaff74-997c-47c2-ac26-4cd7f0bf4379" />
<img width="622" height="284" alt="Screenshot 2026-07-02 160550" src="https://github.com/user-attachments/assets/9c23064e-46dc-4082-b219-f9188e3815d4" />


<img width="904" height="340" alt="Screenshot 2026-07-02 160632" src="https://github.com/user-attachments/assets/dd5c0ce0-15f5-4f76-a252-a98c1ce5ee77" />
<img width="565" height="227" alt="Screenshot 2026-07-02 160638" src="https://github.com/user-attachments/assets/3b21a1af-3b83-4f59-8cd9-9bc1f51875b9" />


MULTI-AGENTS:
<img width="908" height="390" alt="Screenshot 2026-07-02 160739" src="https://github.com/user-attachments/assets/2df97617-6322-4932-a9f5-dbae4e3e7fa8" />
<img width="616" height="257" alt="Screenshot 2026-07-02 160746" src="https://github.com/user-attachments/assets/a98d82d1-e5e4-4628-97fa-c778c24feb62" />


The agents are :
<img width="128" height="70" alt="image" src="https://github.com/user-attachments/assets/0666196b-9f62-4fbb-a613-23e1b62ebb8f" />

The LLM model assesses the question and decides which agent to use depending on the intent of the user question and calls tools


# Insurance Policy RAG + Agentic AI

This project is an AI-powered insurance policy assistant that answers user queries using Retrieval-Augmented Generation (RAG) and a custom multi-agent architecture.

The system retrieves relevant information from an insurance policy PDF and uses a GPT-based Router Agent to decide which specialist agent(s) should answer the user's query.

## Features

- Insurance policy question answering
- Retrieval-Augmented Generation (RAG)
- Custom multi-agent architecture
- GPT-based Router Agent
- Policy, Eligibility, Benefit, Checklist, Grievance and Exclusion agents
- OpenRouter GPT integration
- FastAPI backend

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- PyPDF
- RecursiveCharacterTextSplitter
- Sentence Transformers (all-MiniLM-L6-v2)
- OpenRouter GPT

## Project Structure

```
backend/
│
├── agents/
├── llm/
├── routes/
├── tools/
├── rag/
└── main.py
```

## Setup

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_api_key
```

Run the application

```bash
uvicorn backend.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## Example Queries

- What is the deductible?
- Is my child's accident covered?
- My ER bill was $600. How much can I claim?
- What documents do I need to submit?
- My claim was rejected. How can I appeal?

## Note

This project uses a **custom multi-agent architecture** and does **not** use LangGraph or CrewAI.
