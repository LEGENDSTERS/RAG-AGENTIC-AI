from backend.agents.agent_utils import run_agent


def eligibility_agent(question: str):

    system_prompt = """
You are an insurance eligibility specialist.
"""

    task_prompt = """
Determine whether the claim is covered.

Rules:

- Use ONLY the policy.
- Explain briefly.
- If policy does not specify, say:

'I could not determine eligibility from the policy.'
"""

    return run_agent(
        question,
        system_prompt,
        task_prompt
    )