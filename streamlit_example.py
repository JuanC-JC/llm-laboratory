import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

st.title("Lukita")

# Set OpenAI API key from Streamlit secrets
client = ChatOllama(model="llama3.2")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


# Display assistant response in chat message container
with st.chat_message("assistant"):
    message_placeholder = st.empty()

    historyMessages = ChatPromptTemplate([
      ("system", "You are a helpful assistant"),
      MessagesPlaceholder("messagesHistory")
    ])

    chain = historyMessages | client
    full_response = ""
    # Convert session messages to format expected by chain
    messages_for_chain = {
        "messagesHistory": [
            {
                "role": message["role"],
                "content": message["content"]
            }
            for message in st.session_state.messages
        ]
    }

    # Stream response chunks and update display
    for chunk in chain.stream(messages_for_chain):
        full_response += chunk.content
        # Show blinking cursor effect while streaming
        message_placeholder.markdown(full_response)

    full_response = full_response.strip()

    # message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})