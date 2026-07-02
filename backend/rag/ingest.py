import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "..", "documents", "insurance_policy.pdf")
CHROMA_DIR = os.path.join(BASE_DIR, "chromadb")


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
COLLECTION = "insurance_policy"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"



def extract_pages(pdf_path):
    reader = PdfReader(pdf_path)

    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"\n===== PAGE {i+1} =====")
        print(text[:1000] if text else "NO TEXT")

        if text:
            pages.append(
                {
                    "page": i + 1,
                    "text": text.strip()
                }
            )

    print(f"[ingest] Extracted {len(pages)} pages.")
    return pages



def chunk_pages(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []
    idx = 0

    for page in pages:
        pieces = splitter.split_text(page["text"])

        for piece in pieces:
            chunks.append({
                "id": f"chunk_{idx}",
                "text": piece,
                "page": page["page"]
            })
            idx += 1

    print(f"[ingest] Created {len(chunks)} chunks.")
    return chunks





def embed_and_store(chunks):

    print(f"[ingest] Loading embedding model: {EMBED_MODEL} ...")
    model = SentenceTransformer(EMBED_MODEL)

    texts = [c["text"] for c in chunks]

    print("[ingest] Generating embeddings ...")
    embeddings = model.encode(
        texts,
        show_progress_bar=True
    ).tolist()

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    existing = [c.name for c in client.list_collections()]
    if COLLECTION in existing:
        client.delete_collection(COLLECTION)
        print(f"[ingest] Deleted existing collection '{COLLECTION}'.")

    collection = client.create_collection(
        name=COLLECTION,
        metadata={"hnsw:space": "cosine"}
    )

    collection.add(
        ids=[c["id"] for c in chunks],
        embeddings=embeddings,
        documents=texts,
        metadatas=[
            {
                "page": c["page"]
            }
            for c in chunks
        ]
    )

    print(
        f"[ingest] Stored {len(chunks)} chunks in ChromaDB at '{CHROMA_DIR}'."
    )



if __name__ == "__main__":

    pages = extract_pages(PDF_PATH)

    chunks = chunk_pages(pages)

    embed_and_store(chunks)

    print("[ingest] ✅ Ingestion complete.")