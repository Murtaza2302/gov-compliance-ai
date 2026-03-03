def build_final_output(state):

    analysis = state.get("analysis", {})
    draft = state.get("draft", {})
    critic = state.get("critic", {})

    clause_refs = []

    for c in analysis.get("extracted_clauses", []):
        clause_refs.append({
            "source": c["source"],
            "clause_id": c.get("clause_id"),
            "snippet": c["text"][:150]
        })

    final_output = {
        "human_draft": draft.get("human_draft", ""),
        "structured_summary": {
            "query": state.get("query"),
            "total_clauses_used": len(clause_refs)
        },
        "clause_references": clause_refs,
        "compliance_status": critic.get("compliance_status"),
        "violations": critic.get("violations"),
        "confidence_score": critic.get("confidence_score")
    }

    return final_output
