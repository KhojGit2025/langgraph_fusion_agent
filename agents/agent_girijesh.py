from llm import llm
from state import GraphState
from tools.mailtrap_reader import fetch_latest_email

def agent_girijesh(state: GraphState) -> GraphState:
    # ✅ Use existing email from state if present, else fetch a new one
    email_content = state.get("inbox_email") or fetch_latest_email.invoke({})

    # ✅ Debug print to confirm input
    print("\n📩 Girijesh is analyzing this email:\n", email_content)

    # ✅ Ask GPT to interpret the email
    interpretation = llm.invoke([
        {"role": "system", "content": "You are Girijesh, an AI agent who reads and summarizes user emails briefly, and extracts the user's intent or action request."},
        {"role": "user", "content": f"Read this email and summarize the user's intent:\n\n{email_content}"}
    ])

    # ✅ Save email and interpretation to state
    state["inbox_email"] = email_content
    state["messages"].append({"role": "girijesh", "content": interpretation.content})

    return state
