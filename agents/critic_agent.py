def critic_agent(state):

    draft = state.get("draft", {})
    analysis = state.get("analysis", {})

    violations = []

    # Rule 1: Draft must contain extracted clauses
    if not analysis.get("extracted_clauses"):
        violations.append("No clauses retrieved from documents.")

    # Rule 2: Draft must mention at least one source
    draft_text = draft.get("human_draft", "")

    sources = [
        c["source"]
        for c in analysis.get("extracted_clauses", [])
    ]

    source_found = any(src in draft_text for src in sources)

    if not source_found:
        violations.append("Draft does not reference source documents.")

    # Rule 3: Draft too short
    if len(draft.get("human_draft", "")) < 200:
        violations.append("Draft appears incomplete.")

    if violations:
        status = "FAIL"
        confidence = 0.6
    else:
        status = "PASS"
        confidence = 0.9

    return {
        "agent": "critic",
        "compliance_status": status,
        "violations": violations,
        "confidence_score": confidence
    }


if __name__ == "__main__":

    test_state = {
        "analysis": {"extracted_clauses": []},
        "draft": {"human_draft": "Test"}
    }

    print(critic_agent(test_state))