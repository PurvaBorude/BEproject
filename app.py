import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Mental Health Chatbot", layout="wide", page_icon="💬")

# Custom CSS for enhanced visuals with a gradient background
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #e6f7ff, #ffffff); /* Soft gradient */
        font-family: 'Arial', sans-serif;
    }
    .main {
        max-width: 600px;
        margin: auto;
    }
    .chat-container {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
        height: 500px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
    }
    .chat {
        margin: 10px 0;
        padding: 10px 15px;
        border-radius: 15px;
        font-size: 16px;
        max-width: 75%;
        word-wrap: break-word;
    }
    .user {
        align-self: flex-end;
        background-color: #e0f7d4; /* Light green */
        color: #004d00; /* Dark green text */
    }
    .bot {
        align-self: flex-start;
        background-color: #f2f4f5; /* Light gray */
        color: #333333; /* Dark gray text */
    }
    .input-container {
        display: flex;
        align-items: center;
        margin-top: 15px;
    }
    input[type="text"] {
        flex: 1;
        border: none;
        border-radius: 25px;
        padding: 15px;
        font-size: 16px;
        margin-right: 10px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        outline: none;
    }
    button {
        background-color: #25d366;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        cursor: pointer;
    }
    button:hover {
        background-color: #20b857;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Persistent session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
st.write("## 🌟 Mental Health Chatbot")
st.markdown("---")
chat_container = st.container()
with chat_container:
    chat_history = st.empty()
    messages_html = '<div class="chat-container">'
    for message in st.session_state["messages"]:
        role_class = "user" if message["user"] else "bot"
        messages_html += f'<div class="chat {role_class}">{message["text"]}</div>'
    messages_html += "</div>"
    chat_history.markdown(messages_html, unsafe_allow_html=True)

# Input and button
with st.container():
    with st.form("user_input", clear_on_submit=True):
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        user_input = st.text_input("Type your message...", placeholder="Ask me anything...", label_visibility="collapsed")
        submit = st.form_submit_button("Send")
        st.markdown('</div>', unsafe_allow_html=True)

# Handle user input
if submit and user_input:
    # Append user message
    st.session_state["messages"].append({"user": True, "text": user_input})

    # Generate bot response (placeholder)
    bot_response = f"I'm here to help. You said: {user_input}"
    st.session_state["messages"].append({"user": False, "text": bot_response})

    # Refresh chat display
    messages_html = '<div class="chat-container">'
    for message in st.session_state["messages"]:
        role_class = "user" if message["user"] else "bot"
        messages_html += f'<div class="chat {role_class}">{message["text"]}</div>'
    messages_html += "</div>"
    chat_history.markdown(messages_html, unsafe_allow_html=True)
