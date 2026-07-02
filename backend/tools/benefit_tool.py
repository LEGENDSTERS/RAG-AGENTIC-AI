from backend.tools.retrieval_tool import retrieve_context


def get_benefit_context(question: str):
    """
    Retrieves the most relevant policy clauses related to
    benefits, reimbursements, claim limits and payouts.
    """

    return retrieve_context(question)