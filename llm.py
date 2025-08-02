# llm.py
from langchain_openai import ChatOpenAI
from config.load_env import load_env_vars

load_env_vars()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
