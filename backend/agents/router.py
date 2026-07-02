from backend.agents.registry import AGENTS
from backend.agents.response_generator import response_generator
import json
from backend.llm.llm_client import chat


import json
from backend.llm.llm_client import chat


def classify_intent(question: str):

    prompt = f"""
You are the Planner (Router Agent) of an Agentic AI Insurance Assistant.

Your job is NOT to answer the user's question.

Your ONLY job is to create an execution plan.

Available specialist agents:

1. policy_agent
Purpose:
Answers general questions about the insurance policy.

2. eligibility_agent
Purpose:
Determines whether a treatment, accident or situation is covered.

3. benefit_agent
Purpose:
Determines reimbursement amount, claim amount, payout or benefit.

4. checklist_agent
Purpose:
Provides required claim documents.

5. grievance_agent
Purpose:
Handles rejected claims, appeals and grievances.

6. exclusion_agent
Purpose:
Checks policy exclusions.

Rules:

- Think carefully.
- You may select ONE or MORE agents.
- Return ONLY valid JSON.
- Do NOT explain outside the JSON.
- Do NOT use markdown.

Return EXACTLY in this format:

{{
    "plan":[
        {{
            "agent":"policy_agent",
            "reason":"Why this agent is required."
        }}
    ]
}}

Examples

Question:
What is the deductible?

Output:

{{
    "plan":[
        {{
            "agent":"policy_agent",
            "reason":"The user is asking about a policy detail."
        }}
    ]
}}

Question:
My ER bill was $600.
Is it covered?
How much can I claim?

Output:

{{
    "plan":[
        {{
            "agent":"eligibility_agent",
            "reason":"The user wants to know if the treatment is covered."
        }},
        {{
            "agent":"benefit_agent",
            "reason":"The user wants to know the reimbursement amount."
        }}
    ]
}}

Question:

{question}
"""

    response = chat(prompt)

    try:

        result = json.loads(response)

        return result["plan"]

    except Exception:

        print("\nInvalid JSON from Router:\n")
        print(response)

        return [
            {
                "agent": "policy_agent",
                "reason": "Fallback"
            }
        ]

def router_agent(question: str):

    plan = classify_intent(question)
    print("\n==============================")
    print("      ROUTER AGENT")
    print("==============================")
    print(f"Question : {question}")
    print("Execution Plan")

    for step in plan:
        print(step)
    print("==============================")

    results = []

    for step in plan:

        agent = step["agent"]
        reason = step["reason"]

        print(f"\nExecuting: {agent}")
        print(f"Reason    : {reason}")

        if agent not in AGENTS:
            print(f"Unknown agent: {agent}")
        continue

    result = AGENTS[agent](question)
    results.append(result)

    # If only one agent executed, return it directly.
    if len(results) == 1:
        return results[0]

    # Combine outputs from multiple agents.
    agent_outputs = ""

    for i, result in enumerate(results, start=1):

        agent_outputs += f"""
Agent {i}

{result["answer"]}

"""

    final_answer = response_generator(
        question,
        agent_outputs
    )

    return {
        "answer": final_answer
    }