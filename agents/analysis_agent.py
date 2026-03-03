import re
from rag.retriever import retrieve


def analysis_agent(query):
    """
    Analysis Agent:
    - Retrieves relevant chunks using RAG
    - Extracts clause/rule identifiers
    - Filters out non-legal chunks
    - Ensures fallback if no clause IDs detected
    """

    results = retrieve(query)

    extracted = []

    for r in results:

        text = r["text"]

        rule_match = re.search(r"(Rule\s*\d+(\.\d+)*)", text)

        section_match = re.search(r"\b\d+\.\d+(\.\d+)*\b", text)

        clause_id = None

        if rule_match:
            clause_id = rule_match.group(0)
        elif section_match:
            clause_id = section_match.group(0)

        if clause_id is not None:
            extracted.append({
                "source": r["source"],
                "clause_id": clause_id,
                "text": text[:400]
            })

    if not extracted:
        for r in results[:1]:
            extracted.append({
                "source": r["source"],
                "clause_id": None,
                "text": r["text"][:400]
            })

    return {
        "agent": "analysis",
        "query": query,
        "extracted_clauses": extracted
    }

if __name__ == "__main__":

    query = "procurement under 25 lakh"

    output = analysis_agent(query)

    print("\nANALYSIS OUTPUT:\n")
    print(output)