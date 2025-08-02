# tools/email_tool.py

import os
from langchain_core.tools import tool
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from config.load_env import load_env_vars

# ✅ Load environment variables (like MAILTRAP_USERNAME and PASSWORD)
load_env_vars()

@tool
def send_email_tool(to: str, subject: str, body: str) -> str:
    """
    Sends an email using Mailtrap SMTP. Requires recipient address, subject, and body.
    """
    SMTP_SERVER = "sandbox.smtp.mailtrap.io"
    SMTP_PORT = 587
    USERNAME = os.getenv("MAILTRAP_USERNAME")
    PASSWORD = os.getenv("MAILTRAP_PASSWORD")

    # ✅ Check if credentials are present
    if not USERNAME or not PASSWORD:
        return "❌ Email credentials not found. Check your .env file."

    sender_email = "agent@langgraph.ai"

    # ✅ Construct the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # ✅ Send the email via Mailtrap
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)

        return f"✅ Email sent successfully to {to}"
    except Exception as e:
        return f"❌ Failed to send email: {str(e)}"
