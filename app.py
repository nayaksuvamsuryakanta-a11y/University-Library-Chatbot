# app.py
import streamlit as st
from library_chatbot import process_query


st.set_page_config(page_title="University Library Chatbot")

st.title("📚 University Library Chatbot")
st.write("Ask me about book availability, renewals, fines, and more!")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
if prompt := st.chat_input("Your message..."):
    # Show user's message immediately
    with st.chat_message("user"):
        st.write(prompt)

    # Generate bot response
    with st.spinner("Thinking..."):
        response, st.session_state.messages = process_query(
            prompt,
            st.session_state.messages
        )

    # Show assistant response
    with st.chat_message("assistant"):
        st.write(response)