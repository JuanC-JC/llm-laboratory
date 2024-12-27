from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from helpers.streamlit_chat_helper import helper_streamlit_chat
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
template = """
Eres Lukita, un asistente virtual especializado en finanzas del hogar y gestión doméstica.
Debes responder siempre como Lukita, de manera amigable y práctica, ayudando a los usuarios con:
- Preguntas sobre presupuestos familiares
- Consejos sobre ahorro en el hogar
- Consultas generales sobre administración doméstica
- Sugerencias prácticas para la economía familiar

Recuerda: Tú eres Lukita y debes responder al usuario de forma cercana y con lenguaje sencillo.

Pregunta del usuario: {question}
"""

def chat_with_ollama() -> str:
    ollama = ChatOllama(model="llama3.2")
    system_message = SystemMessage(content=template)
    # human_message = HumanMessage(content=question)

    historyMessages = ChatPromptTemplate([
        system_message,
        MessagesPlaceholder("messagesHistory")
    ])

    chain = historyMessages | ollama

    # messages = [system_message] + chat_history + [human_message]
    # return ollama.invoke(, system_message=system_message)

    helper_streamlit_chat(chain)


chat_with_ollama()