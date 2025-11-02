import streamlit as st
import uuid
from datetime import datetime

# Page setup
st.set_page_config(page_title="Digital Receipt Generator", layout="centered")

# Branding
st.markdown("### Vikas Bhosale TYIT 19009")
st.title("🧾 Digital Receipt Generator")

# Input form
sender = st.text_input("Sender Name")
receiver = st.text_input("Receiver Name")
amount = st.text_input("Amount")

# Generate receipt
if st.button("Generate Receipt"):
    if not sender or not receiver or not amount:
        st.error("All fields are required.")
    else:
        receipt_id = str(uuid.uuid4())[:8].upper()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success("Receipt Generated!")

        # Styled receipt block
        st.markdown(
            f"""
            <div style="background-color:#333333; padding:15px; border-radius:10px; color:#ffffff;">
                <p><strong>Receipt ID:</strong> {receipt_id}</p>
                <p><strong>Date:</strong> {timestamp}</p>
                <p><strong>Sender:</strong> {sender}</p>
                <p><strong>Receiver:</strong> {receiver}</p>
                <p><strong>Amount:</strong> ₹{amount}</p>
            </div>
            """, unsafe_allow_html=True
        )
