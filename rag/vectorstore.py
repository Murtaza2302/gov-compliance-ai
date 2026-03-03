import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from chunker import chunk_documents


def build_vectorstore():

    print("Loading chunks...")
    chunks = chunk_documents()

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [c["text"] for c in chunks]

    print("Creating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    print("Building FAISS index...")
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, "rag/faiss_index.index")

    # Save chunks separately
    with open("rag/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Vectorstore built successfully!")


if __name__ == "__main__":
    build_vectorstore()