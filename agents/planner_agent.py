def planner_agent(user_query):

    plan = {
        "agent": "planner",
        "user_query": user_query,
        "tasks": [
            "retrieve relevant clauses using RAG",
            "analyze rules and authorities",
            "draft compliance note",
            "validate compliance"
        ]
    }

    return plan


if __name__ == "__main__":

    query = "Draft compliance note for procurement under 25 lakh"

    output = planner_agent(query)

    print(output)