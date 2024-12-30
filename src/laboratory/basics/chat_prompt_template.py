from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from src.helpers.chat_helper import chat_helpers

tutor_template = ChatPromptTemplate.from_messages([
    ("system", "Eres un tutor paciente que explica conceptos de {subject}"),
    ("user", "{student_question}"),
])

def chat_with_ollama(question: str, history: None) -> str:
    ollama = ChatOllama(model="llama3.2")
    chain = tutor_template | ollama
    response = chain.invoke({"subject": "matemáticas", "student_question": question})
    return response

def main():
    conversation = []
    chat_metadata = {
        "file_name": __file__,
        "agent_type": "tutor",
        "subject": "matemáticas",
        "language": "spanish"
    }

    chat_helpers(chat_with_ollama, conversation, chat_metadata, "llama3.2")

if __name__ == "__main__":
    main()
