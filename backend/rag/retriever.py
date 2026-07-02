import os
from sentence_transformers import SentenceTransformer
import chromadb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DIR = os.path.join(BASE_DIR, "chromadb")
COLLECTION = "insurance_policy"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 4


class Retriever:
    def __init__(self):
        print("[retriever] Loading embedding model ...")

        self.model = SentenceTransformer(EMBED_MODEL)

        self.client = chromadb.PersistentClient(path=CHROMA_DIR)
        self.collection = self.client.get_collection(COLLECTION)

        print(
            f"[retriever] Connected to collection '{COLLECTION}' "
            f"({self.collection.count()} chunks)."
        )

    def get_relevant_chunks(self, query: str, top_k: int = TOP_K) -> list[str]:

        
        query_embedding = self.model.encode(query).tolist()

        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "distances", "metadatas"]
        )

        chunks = results["documents"][0]
        distances = results["distances"][0]

        print("\n===== RETRIEVED CHUNKS =====")
        print(f"Query: {query}")

        for i, (chunk, dist) in enumerate(zip(chunks, distances)):
            print(f"\n[{i+1}] Distance = {dist:.4f}")
            print(chunk[:300])
            print("-------------------------")

        return chunks