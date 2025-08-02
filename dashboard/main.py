# dashboard/main.py

import sys
import os

# ✅ Add project root to sys.path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from email_tab import email_tab  # ✅ Must be in dashboard/email_tab.py

def main():
    st.set_page_config(
        page_title="LangGraph Fusion Agent Dashboard",
        layout="wide"
    )
    st.title("LangGraph Fusion Agent Dashboard")

    # ✅ Single tab layout — safely unpacked
    tab1, = st.tabs(["📧 Email Interface"])
    with tab1:
        email_tab()

if __name__ == "__main__":
    main()

#Command for stremlite dashboard runing---->   streamlit run dashboard/main.py