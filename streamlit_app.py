import streamlit as st
import qrcode
from io import BytesIO

st.title("🔗 QR Code Generator")

# The URL input
link = st.text_input("Enter your URL:", "https://hanshhilar705.wixsite.com/qrconect")

if link:
    qr = qrcode.make(link)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    st.image(buf.getvalue(), width=300)
    st.download_button("Download QR", buf.getvalue(), "qr.png", "image/png")