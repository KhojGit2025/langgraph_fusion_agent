from state import GraphState

def agent_amit(state: GraphState) -> GraphState:
    result = state.get("email_result", "")
    summary = f"Amit reviewed tool output. Email status: {result}"
    state["messages"].append({"role": "assistant", "content": summary})
    return state
