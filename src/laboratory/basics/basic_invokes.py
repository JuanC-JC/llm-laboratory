from langchain_ollama import ChatOllama

def chat_with_ollama(prompt: str) -> str:
    ollama = ChatOllama(model="llama3.2")
    return ollama.invoke(prompt)


if __name__ == "__main__":
    user_input = input("Enter your question: ")
    print(chat_with_ollama(user_input))
