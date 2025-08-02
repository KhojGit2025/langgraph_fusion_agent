import streamlit as st


def whatsapp_tab():
    st.subheader("💬 WhatsApp Interface (Prototype)")

    # --- SEND WHATSAPP --- #
    st.markdown("### 📤 Send WhatsApp Message")
    phone_number = st.text_input("Phone Number:", placeholder="+91XXXXXXXXXX")
    message = st.text_area("Message:")

    if st.button("Send WhatsApp Message"):
        if phone_number and message:
            st.info("[Mock] WhatsApp message sent. [Integration needed]")
        else:
            st.warning("Please enter phone number and message.")

    # --- VIEW RECEIVED (Future) --- #
    st.markdown("---")
    st.markdown("### 📥 Incoming Messages")
    st.info("Incoming WhatsApp message display will be implemented via webhook polling or Twilio.")
