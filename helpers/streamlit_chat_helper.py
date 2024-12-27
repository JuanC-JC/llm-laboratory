import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage


def helper_streamlit_chat(chain_to_invoke):
    # # Set OpenAI API key from Streamlit secrets
    # client = ChatOllama(model="llama3.2")

    st.title("Lukita")

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


    full_response = ""
    # Convert session messages to format expected by chain
    messages_for_chain = {
        "messagesHistory": [
            {**message}
            for message in st.session_state.messages
        ]
    }

    print(messages_for_chain)

    final_response = None
    # Stream response chunks and update display
    for chunk in chain_to_invoke.stream(messages_for_chain):
        full_response += chunk.content
        # Show blinking cursor effect while streaming
        message_placeholder.markdown(full_response)
        final_response = chunk
        print("\nany chunk", chunk)

    print("\nfinal_response", final_response)
    full_response = full_response.strip()

    # message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})