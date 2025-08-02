import os
import requests
from langchain_core.tools import tool
from config.load_env import load_env_vars

load_env_vars()

@tool
def fetch_latest_email() -> dict:
    """Fetches the most recent email from Mailtrap inbox via API and returns sender, subject, and body."""
    INBOX_ID = os.getenv("MAILTRAP_INBOX_ID")
    ACCOUNT_ID = os.getenv("MAILTRAP_ACCOUNT_ID")
    API_TOKEN = os.getenv("MAILTRAP_API_TOKEN")

    if not (INBOX_ID and ACCOUNT_ID and API_TOKEN):
        return {"error": "❌ Missing MAILTRAP credentials. Check .env file."}

    headers = {"Api-Token": API_TOKEN}
    list_url = f"https://mailtrap.io/api/accounts/{ACCOUNT_ID}/inboxes/{INBOX_ID}/messages"

    try:
        # Step 1: Get list of emails
        response = requests.get(list_url, headers=headers)
        response.raise_for_status()
        messages = response.json()

        if not messages:
            return {"error": "⚠️ Inbox is empty."}

        latest = messages[0]
        latest_id = latest["id"]
        from_email = latest.get("from_email", "Unknown sender")
        subject = latest.get("subject", "No subject")

        # Step 2: Fetch body of the latest email
        detail_url = f"https://mailtrap.io/api/accounts/{ACCOUNT_ID}/inboxes/{INBOX_ID}/messages/{latest_id}/body.txt"
        body_response = requests.get(detail_url, headers=headers)
        body_response.raise_for_status()
        body_text = body_response.text.strip()

        return {
            "from_email": from_email,
            "subject": subject,
            "body": body_text
        }

    except Exception as e:
        return {"error": f"❌ Failed to fetch email: {str(e)}"}
