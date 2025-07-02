
import streamlit as st

st.set_page_config(page_title="Project X", layout="wide")

# -------------------------------
# 🎵 Sample Song Database
# -------------------------------
songs = [
    {"title": "Raabta", "artist": "Pritam", "price": 102, "return": "+4.5%", "cover": "🎶"},
    {"title": "Kesariya", "artist": "Pritam", "price": 98, "return": "-1.2%", "cover": "🌅"},
    {"title": "Apna Bana Le", "artist": "Sachin-Jigar", "price": 110, "return": "+6.2%", "cover": "💑"},
    {"title": "Tum Hi Ho", "artist": "Mithoon", "price": 89, "return": "-3.8%", "cover": "💔"},
    {"title": "Channa Mereya", "artist": "Arijit Singh", "price": 120, "return": "+3.1%", "cover": "🎤"},
    {"title": "Ilahi", "artist": "Pritam", "price": 95, "return": "-2.5%", "cover": "🌍"},
]

if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}

# -------------------------------
# 🔍 Search Bar
# -------------------------------
search_query = st.sidebar.text_input("🔍 Search Song or Artist").lower()

if search_query:
    filtered_songs = [s for s in songs if search_query in s["title"].lower() or search_query in s["artist"].lower()]
else:
    filtered_songs = songs

# -------------------------------
# 🎵 Song Marketplace
# -------------------------------
st.title("🎵 Project X – Music as Trading MVP")

cols = st.columns(3)
for idx, song in enumerate(filtered_songs):
    with cols[idx % 3]:
        st.markdown(f"## {song['cover']} {song['title']}")
        st.caption(f"by *{song['artist']}*")
        st.metric("Price", f"₹{song['price']}", song['return'])

        if st.button(f"📥 Buy", key=f"buy_{idx}"):
            if song['title'] not in st.session_state.portfolio:
                st.session_state.portfolio[song['title']] = {"artist": song['artist'], "qty": 1, "price": song['price']}
            else:
                st.session_state.portfolio[song['title']]["qty"] += 1

        if st.button(f"📤 Sell", key=f"sell_{idx}"):
            if song['title'] in st.session_state.portfolio and st.session_state.portfolio[song['title']]["qty"] > 0:
                st.session_state.portfolio[song['title']]["qty"] -= 1
                if st.session_state.portfolio[song['title']]["qty"] == 0:
                    del st.session_state.portfolio[song['title']]

# -------------------------------
# 👤 User Profile Dashboard
# -------------------------------
st.markdown("---")
st.subheader("👤 Your Profile & Holdings")

if st.session_state.portfolio:
    for title, data in st.session_state.portfolio.items():
        current_price = next((s["price"] for s in songs if s["title"] == title), 0)
        holding_value = data["qty"] * current_price
        st.write(f"🎵 **{title}** by {data['artist']} — Quantity: {data['qty']} | Value: ₹{holding_value}")
else:
    st.info("You don't own any song shares yet.")
