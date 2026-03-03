import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("rag/faiss_index.index")

# Load chunks
with open("rag/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve(query, top_k=3):

    # Encode query
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Retrieve more candidates first
    distances, indices = index.search(query_embedding, 10)

    candidate_chunks = [chunks[i] for i in indices[0]]

    # Smart filtering keywords
    keywords = [
        "rule",
        "clause",
        "section",
        "₹",
        "lakh",
        "procurement",
        "approval",
        "authority"
    ]

    filtered = []

    for chunk in candidate_chunks:
        text_lower = chunk["text"].lower()

        if any(keyword in text_lower for keyword in keywords):
            filtered.append(chunk)

    # If filtering too strict, fallback to candidates
    if len(filtered) < top_k:
        filtered = candidate_chunks

    return filtered[:top_k]

if __name__ == "__main__":

    query = "procurement under 25 lakh"

    results = retrieve(query)

    for i, r in enumerate(results):
        print("\n====================")
        print("Result", i + 1)
        print("Source:", r["source"])
        print(r["text"][:500])