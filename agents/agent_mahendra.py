from state import GraphState
from tools.email_tool import send_email_tool
from llm import llm

def agent_mahendra(state: GraphState) -> GraphState:
        # 👇 Use Girijesh's interpreted summary
    latest = state["messages"][-1]["content"]

  # 🧠 GPT prompt for subject + body
    email_prompt = f"""
You are Mahendra, an AI agent responsible for replying to the email topic suggested by Agent Girijesh.

Message summary:
{latest}
    Now write:
1. A short subject line relevant to the message.
2. A professional reply body in under 100 words.
Return output in the format:
Subject: <subject>
Body: <body>
"""
    llm_response = llm.invoke([
        {"role": "system", "content": "You are a helpful assistant who replies to professional emails."},
        {"role": "user", "content": email_prompt.strip()}
    ])

    # 🔍 Parse GPT output
    output = str(llm_response.content).strip()
    try:
        subject_line = output.split("Subject:")[1].split("Body:")[0].strip()
        body_text = output.split("Body:")[1].strip()
    except Exception:
        subject_line = "Follow-up Email"
        body_text = output

    # 📧 Send email
    result = send_email_tool.invoke({
        "to": "khojbest@gmail.com",
        "subject": subject_line,
        "body": body_text
    })

    # 🗂️ Update state
    state["email_result"] = result
    state["messages"].append({"role": "tool", "content": f"Mahendra sent email. Result: {result}"})
    return state