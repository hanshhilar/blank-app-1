import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Tag Factory", page_icon="🎨")

st.title("🎨 QR Tag Factory")

# --- 1. CONFIGURATION ---
with st.container(border=True):
    st.subheader("Configure your QR")
    
    # Selection for what kind of QR to make
    mode = st.radio("What should this QR do?", ["Contact Owner Link", "Custom URL"])
    
    if mode == "Contact Owner Link":
        st.info("This will create a link that automatically fills the owner's email in your form.")
        owner_email = st.text_input("Owner's Email Address:", "hanshhilar705@gmail.com")
        # Use your ACTUAL app URL here
        base_url = "https://blank-app-x4koreu3hsq.streamlit.app/contact"
        final_link = f"{base_url}?owner={owner_email}"
    else:
        final_link = st.text_input("Enter URL:", "https://")

    qr_label = st.text_input("Label (e.g., 'My Backpack'):", "My Item")

# --- 2. GENERATION LOGIC ---
if st.button("✨ Generate QR Code", use_container_width=True):
    if not final_link or final_link == "https://":
        st.error("Please provide a valid link or email.")
    else:
        # Create QR
        qr = qrcode.make(final_link)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        
        st.divider()
        st.success(f"Generated for: {qr_label}")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(buf.getvalue(), width=250)
        with col2:
            st.write(f"**Target URL:** `{final_link}`")
            st.download_button(
                "💾 Download PNG",
                buf.getvalue(),
                f"{qr_label.replace(' ', '_')}_qr.png",
                "image/png"
            )