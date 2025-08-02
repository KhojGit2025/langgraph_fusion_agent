from graph_builder import build_graph
from tools.mailtrap_reader import fetch_latest_email

# 📨 Fetch latest email from Mailtrap
latest_email = fetch_latest_email.invoke({})

# 🧠 Build LangGraph
app = build_graph()

# ⚙️ Prepare initial state with real input
initial_state = {
    "messages": [],
    "inbox_email": latest_email,  # ✅ Important for agent_girijesh
    "email_result": None,
    "calendar_result": None,
    "file_result": None,
    "whatsapp_result": None,
    "call_result": None,
    "web_result": None
}

final_state = app.invoke(initial_state, config={"recursion_limit": 5})

print("\nFinal Output:")
for msg in final_state["messages"]:
    print(f'{msg["role"]}: {msg["content"]}')
