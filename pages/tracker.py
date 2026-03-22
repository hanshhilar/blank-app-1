import streamlit as st
import time

# Styling to match your Wix Navy and Orange
st.set_page_config(page_title="Item Safety Check", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #002060; color: white; text-align: center; }
    h1 { color: #FF8C00; }
    .stMetric { background-color: #ffffff20; border-radius: 15px; padding: 10px; }
    </style>
    """, unsafe_allow_value=True)

st.title("🛡️ Item Verified")
st.subheader("Your belongings are safe.")

# Safety Timer
st.write("Next check-in required in:")
placeholder = st.empty()

# 30-minute commute timer
for i in range(1800, 0, -1):
    mins, secs = divmod(i, 60)
    placeholder.metric("Time Remaining", f"{mins:02d}:{secs:02d}")
    time.sleep(1)
    if i == 1:
        st.error("⚠️ ALERT: Time up! Please re-scan your item.")