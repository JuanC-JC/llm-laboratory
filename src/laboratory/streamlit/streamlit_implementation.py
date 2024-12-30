from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from helpers.streamlit_chat_helper import helper_streamlit_chat

model = ChatOllama(model="llama3.2")

historyMessages = ChatPromptTemplate([
    ("system", "Eres un perrito que habla español"),
    MessagesPlaceholder("messagesHistory")
])

chain = historyMessages | model

helper_streamlit_chat(chain)