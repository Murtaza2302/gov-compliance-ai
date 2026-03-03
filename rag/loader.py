import os
from pypdf import PdfReader


def load_pdfs(folder_path):
    documents = []

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return documents

    files = os.listdir(folder_path)

    if not files:
        print("No files found in folder.")
        return documents

    print("Files found:", files)

    for file in files:
        if file.lower().endswith(".pdf"):
            path = os.path.join(folder_path, file)

            try:
                reader = PdfReader(path)
                text = ""

                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

                documents.append({
                    "source": file,
                    "text": text
                })

                print(f"Loaded: {file}")

            except Exception as e:
                print(f"Error reading {file}: {e}")

    return documents


if __name__ == "__main__":
    docs = load_pdfs("data/raw_pdfs")
    print(f"\nTotal documents loaded: {len(docs)}")