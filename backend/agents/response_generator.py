from backend.llm.llm_client import chat


def response_generator(question, agent_outputs):

    prompt = f"""
You are the Final Response Generator of an Agentic AI Insurance Assistant.

Your job is to combine the outputs from multiple specialist agents into ONE clear response.

User Question:
{question}

Outputs from Agents:

{agent_outputs}

Instructions:

- Produce ONE final answer.
- Remove duplicate information.
- Keep the response natural and professional.
- Use bullet points where appropriate.
- Do NOT invent facts.
- Use ONLY the information supplied by the agents.
- If different agents provide related information, merge it smoothly.
"""

    return chat(prompt)