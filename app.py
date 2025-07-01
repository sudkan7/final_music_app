
import streamlit as st

st.set_page_config(page_title="Project X", layout="wide")

# Header
st.title("🎵 Project X – Music as Trading MVP")

# Mock song data
songs = [
    {"title": "Raabta", "artist": "Pritam", "price": 102, "return": "+4.5%"},
    {"title": "Kesariya", "artist": "Pritam", "price": 98, "return": "-1.2%"},
    {"title": "Apna Bana Le", "artist": "Sachin-Jigar", "price": 110, "return": "+6.2%"},
    {"title": "Tum Hi Ho", "artist": "Mithoon", "price": 89, "return": "-3.8%"},
]

# Layout
cols = st.columns(len(songs))
for i, song in enumerate(songs):
    with cols[i]:
        st.subheader(song["title"])
        st.caption(f"by {song['artist']}")
        st.metric(label="Current Price", value=f"₹{song['price']}", delta=song["return"])
        if st.button(f"📥 Buy", key=f"buy_{i}"):
            st.success(f"Bought share in {song['title']}")
        if st.button(f"📤 Sell", key=f"sell_{i}"):
            st.warning(f"Sold share in {song['title']}")

# Dashboard
st.markdown("---")
st.subheader("📊 Your Dashboard (Demo)")
st.write("Holdings, average buy price, and P&L would be shown here in next version.")
