import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_pdfs


def chunk_documents():
    docs = load_pdfs("data/raw_pdfs")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for doc in docs:
        split_texts = splitter.split_text(doc["text"])

        for chunk in split_texts:
            chunks.append({
                "text": chunk,
                "source": doc["source"]
            })

    return chunks


if __name__ == "__main__":
    chunks = chunk_documents()
    print(f"Total chunks created: {len(chunks)}")