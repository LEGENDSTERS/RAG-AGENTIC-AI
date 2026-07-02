from backend.tools.retrieval_tool import retrieve_context
from backend.llm.llm_client import chat
import time


def run_agent(
    question: str,
    system_prompt: str,
    task_prompt: str,
    retrieval_function=retrieve_context
):
    """
    Shared helper used by all specialist agents.
    """

    # -------------------------
    # Retrieve relevant chunks
    # -------------------------

    start = time.time()

    chunks = retrieval_function(question)

    retrieval_time = time.time() - start

    print(f"[Agent] Retrieval: {retrieval_time:.2f} sec")

    if not chunks:

        return {
            "answer": "I could not find relevant information in the policy."
        }

    context = "\n\n---\n\n".join(chunks)

    # -------------------------
    # Build Prompt
    # -------------------------

    prompt = f"""
{system_prompt}

{task_prompt}

Policy Context:

{context}

User Question:

{question}

Instructions:

- Answer ONLY using the policy context.
- If the answer is not present, say so.
- Do not hallucinate.
- Keep the answer concise and professional.
"""

    # -------------------------
    # Call LLM
    # -------------------------

    start = time.time()

    answer = chat(prompt)

    llm_time = time.time() - start

    print(f"[Agent] LLM: {llm_time:.2f} sec")

    return {
        "answer": answer
    }