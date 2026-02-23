import streamlit as st
from backend.chatbot import ask_chatbot

st.set_page_config(page_title="AI Career Advisor", layout="wide")

st.title("🎓 AI Career Advisor Chatbot")

# ---------------- Session ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Chat Input ----------------
user_input = st.chat_input("Ask your career question...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    response = ask_chatbot(user_input)

    st.session_state.messages.append(("bot", response))

# ---------------- Display Messages ----------------
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# ---------------- Clear Chat Button (after response) ----------------
if len(st.session_state.messages) > 0:
    st.divider()
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()