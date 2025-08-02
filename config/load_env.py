# config/load_env.py
from dotenv import load_dotenv
import os

def load_env_vars():
    load_dotenv()  # Loads variables from .env file into environment

    # ✅ These are the correct environment variable NAMES
    required_keys = [
        "OPENAI_API_KEY",
        "MAILTRAP_USERNAME",
        "MAILTRAP_PASSWORD",
        "MAILTRAP_API_TOKEN",
        "MAILTRAP_INBOX_ID",
        "MAILTRAP_ACCOUNT_ID"
    ]

    for key in required_keys:
        if not os.getenv(key):
            raise EnvironmentError(f"Missing environment variable: {key}")