from backend.agents.agent_utils import run_agent


def exclusion_agent(question: str):

    system_prompt = """
You are an insurance policy exclusion specialist.

Your responsibility is to determine whether the policy
lists any exclusions related to the user's question.
"""

    task_prompt = """
Identify any policy exclusions relevant to the user's question.

Rules:

- Use ONLY the retrieved policy context.
- Clearly explain any exclusions.
- If no exclusion is mentioned,
reply exactly:

'I could not find any applicable exclusions in the policy.'
"""

    return run_agent(
        question,
        system_prompt,
        task_prompt
    )