from langchain_ollama import OllamaLLM


def drafting_agent(state):

    llm = OllamaLLM(model="llama3:8b-instruct-q4_0")

    query = state["query"]
    clauses = state["analysis"]["extracted_clauses"]

    context = ""

    for c in clauses:
        context += f"\nSource: {c['source']}\n"
        context += c["text"][:150] + "\n"

    prompt = f"""
You are a government procurement compliance assistant.

User request:
{state["query"]}

Relevant clauses retrieved from official documents:
{context}

IMPORTANT REQUIREMENTS:
1. You MUST explicitly mention the source document file names exactly as shown (e.g., Manual_Goods_2024.pdf).
2. If clause_id is available, mention it in the draft.
3. Do NOT invent rules.
4. Write in formal structured compliance format.
5. Ensure at least one source document is referenced clearly.

Now draft the compliance note.
"""

    draft_text = llm.invoke(prompt)

    output = {
        "agent": "drafting",
        "human_draft": draft_text,
        "compliance_status": "PENDING",
        "confidence_score": 0.80
    }

    return output


if __name__ == "__main__":

    test_state = {
        "query": "Draft compliance note for procurement under 25 lakh",
        "analysis": {
            "extracted_clauses": [
                {"source": "GFR_2017.pdf", "text": "Procurement up to 25 lakh..."}
            ]
        }
    }

    print(drafting_agent(test_state))