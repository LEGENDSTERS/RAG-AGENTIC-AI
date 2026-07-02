from backend.rag.retriever import Retriever

# Load Retriever only once
retriever = Retriever()


def retrieve_context(question: str):
    """
    Retrieves the most relevant chunks from the policy.
    """

    return retriever.get_relevant_chunks(question)