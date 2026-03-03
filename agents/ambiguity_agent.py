def ambiguity_agent(state):

    query = state["query"].lower()

    assumptions = []

    # simple checks
    if "lakh" not in query and "crore" not in query:
        assumptions.append("Procurement value not specified; assuming under ₹25 lakh.")

    if "authority" not in query:
        assumptions.append("Approving authority will be inferred from retrieved clauses.")

    if "deadline" not in query:
        assumptions.append("No explicit deadline provided; using standard policy timelines.")

    return {
        "agent": "ambiguity",
        "assumptions": assumptions
    }


if __name__ == "__main__":

    test_state = {
        "query": "Draft compliance note"
    }

    print(ambiguity_agent(test_state))