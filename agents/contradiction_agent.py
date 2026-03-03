import re


def contradiction_agent(state):

    clauses = state["analysis"]["extracted_clauses"]

    contradictions = []

    limits_found = []

    for c in clauses:

        text = c["text"]

        # find numbers like 5 lakh, 25 lakh etc.
        numbers = re.findall(r"\b\d+\s*lakh\b", text.lower())

        for n in numbers:
            limits_found.append({
                "source": c["source"],
                "limit": n
            })

    # simple contradiction check
    unique_limits = set([l["limit"] for l in limits_found])

    if len(unique_limits) > 1:
        contradictions.append({
            "message": "Different procurement limits detected across documents.",
            "limits_found": limits_found
        })

    return {
        "agent": "contradiction",
        "contradictions": contradictions
    }


if __name__ == "__main__":

    test_state = {
        "analysis": {
            "extracted_clauses": [
                {"source": "doc1.pdf", "text": "limit is 5 lakh"},
                {"source": "doc2.pdf", "text": "limit is 25 lakh"}
            ]
        }
    }

    print(contradiction_agent(test_state))