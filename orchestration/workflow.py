import json

from agents.planner_agent import planner_agent
from agents.analysis_agent import analysis_agent
from agents.drafting_agent import drafting_agent
from agents.critic_agent import critic_agent
from agents.contradiction_agent import contradiction_agent
from agents.ambiguity_agent import ambiguity_agent
from orchestration.final_formatter import build_final_output


def run_workflow(user_query):

    state = {
        "query": user_query,
        "plan": None,
        "analysis": None,
        "contradiction": None,
        "ambiguity": None,
        "draft": None,
        "critic": None
    }

    print("\n--- Running Planner Agent ---")
    state["plan"] = planner_agent(user_query)

    print("\n--- Running Ambiguity Agent ---")
    state["ambiguity"] = ambiguity_agent(state)

    max_iterations = 2
    iteration = 0

    while iteration < max_iterations:

        print(f"\n=== ITERATION {iteration + 1} ===")

        print("\n--- Running Analysis Agent ---")
        state["analysis"] = analysis_agent(user_query)

        print("\n--- Running Contradiction Agent ---")
        state["contradiction"] = contradiction_agent(state)

        print("\n--- Running Drafting Agent ---")
        state["draft"] = drafting_agent(state)

        print("\n--- Running Critic Agent ---")
        state["critic"] = critic_agent(state)

        status = state["critic"]["compliance_status"]

        print("\nCompliance Status:", status)

        if status == "PASS":
            print("✔ Draft approved by critic.")
            break

        print("⚠️ Draft failed. Refining...\n")
        iteration += 1

    final_output = build_final_output(state)

    return final_output
    

if __name__ == "__main__":

    print("\n============================================")
    print(" Government Procurement Compliance AI System ")
    print("============================================")

    while True:

        user_query = input("\nEnter your compliance query (or type 'exit'): ")

        if user_query.lower() == "exit":
            print("\nExiting system. Goodbye.")
            break

        result = run_workflow(user_query)

        print("\n============================================")
        print(" HUMAN-READABLE DRAFT ")
        print("============================================\n")

        print(result["human_draft"])

        print("\n============================================")
        print(" STRUCTURED SUMMARY ")
        print("============================================\n")

        structured_view = {
            "query": result["structured_summary"]["query"],
            "total_clauses_used": result["structured_summary"]["total_clauses_used"],
            "compliance_status": result["compliance_status"],
            "confidence_score": result["confidence_score"],
            "violations": result["violations"],
            "clause_references": result["clause_references"]
        }

        print(json.dumps(structured_view, indent=4))

        print("\n============================================")