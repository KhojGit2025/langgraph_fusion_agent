import sys
import os
import streamlit as st

# ✅ Add project root to path for importing modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.email_tool import send_email_tool
from tools.mailtrap_reader import fetch_latest_email

def email_tab():
    st.subheader("📧 Email Interface")

    # --- SEND EMAIL --- #
    st.markdown("### 📤 Send Email")
    to_email = st.text_input("To:", placeholder="example@example.com")
    subject = st.text_input("Subject:")
    body = st.text_area("Body:", height=150)

    if st.button("Send Email"):
        if to_email and subject and body:
            send_email_tool.invoke({
                "to": to_email,
                "subject": subject,
                "body": body
            })
            st.success("✅ Email sent successfully!")
        else:
            st.error("⚠️ Please fill all fields before sending.")

    # --- READ LATEST EMAIL --- #
    st.markdown("---")
    st.markdown("### 📥 Read Latest Email")

    # ✅ Button logic with session state
    if "email_fetch_triggered" not in st.session_state:
        st.session_state.email_fetch_triggered = False

    if st.button("Fetch Latest Email"):
        st.session_state.email_fetch_triggered = True

    if st.session_state.email_fetch_triggered:
        with st.spinner("Fetching latest email..."):
            try:
                result = fetch_latest_email.invoke({})

                if isinstance(result, dict):
                    st.success("✅ Latest email fetched.")
                    st.markdown(f"**From:** {result.get('from_email', 'N/A')}")
                    st.markdown(f"**Subject:** {result.get('subject', 'N/A')}")
                    st.markdown("**Body:**")
                    st.code(result.get("body", "No content."))

                elif isinstance(result, str):
                    st.warning(result)
                else:
                    st.error("⚠️ Unknown response format. Expected dict or str.")

            except Exception as e:
                st.error(f"❌ Exception occurred: {str(e)}")

    # --- RUN AGENT --- #
    st.markdown("---")
    st.markdown("### 🤖 Trigger LangGraph Agent")

    if st.button("Run LangGraph Agent"):
        st.info("⏳ Running agentic graph pipeline...")
        exit_code = os.system("python main.py")
        if exit_code == 0:
            st.success("✅ Agent flow executed successfully.")
        else:
            st.error("❌ Agent flow failed. Check terminal logs.")
