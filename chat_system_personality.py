from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from helpers.chat_helper import chat_helpers

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

def chat_with_ollama(question: str, chat_history: list) -> str:
    ollama = ChatOllama(model="llama3.2")
    system_message = SystemMessage(content=template)
    human_message = HumanMessage(content=question)
    messages = [system_message] + chat_history + [human_message]
    return ollama.invoke(messages)


if __name__ == "__main__":
    chat_history = []

    print("¡Hola! Soy Lukita, tu asistente virtual para finanzas del hogar.")
    print("Escribe 'salir' cuando quieras terminar la conversación.\n")

    chat_helpers(
      invoke_function=chat_with_ollama,
      history=chat_history,
      chat_metadata={
        "file_name": __file__,
        "agent_type": "Lukita",
        "subject": "finanzas del hogar",
        "language": "spanish"
      },
      should_save=True
    )



