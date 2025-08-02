from langgraph.graph import StateGraph, END
from state import GraphState
from agents.agent_girijesh import agent_girijesh
from agents.agent_mahendra import agent_mahendra
from agents.agent_amit import agent_amit

def build_graph():
    builder = StateGraph(GraphState)
    builder.add_node("girijesh", agent_girijesh)
    builder.add_node("mahendra", agent_mahendra)
    builder.add_node("amit", agent_amit)

    builder.set_entry_point("girijesh")
    builder.add_edge("girijesh", "mahendra")
    builder.add_edge("mahendra", "amit")
    builder.add_edge("amit", END)
    return builder.compile()
