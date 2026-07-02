from backend.agents.agent_utils import run_agent


def checklist_agent(question: str):

    system_prompt = """
You are an insurance claim documentation specialist.

Your responsibility is to identify the documents required
to process an insurance claim.
"""

    task_prompt = """
Determine the documents required for the user's claim.

Rules:

- Use ONLY the retrieved policy context.
- List all required documents clearly.
- If the policy does not specify the required documents,
reply exactly:

'I could not find the required claim documents in the policy.'
"""

    return run_agent(
        question,
        system_prompt,
        task_prompt
    )