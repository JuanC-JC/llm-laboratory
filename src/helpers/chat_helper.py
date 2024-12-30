from langchain_core.messages import HumanMessage
from colorama import Fore, Style
from datetime import datetime
from src.helpers.conversation_helper import save_conversation

def chat_helpers(invoke_function, history: list = None, chat_metadata: dict = None, model: str = "", should_save: bool = False):
    metadata = {
        "session_start": datetime.now().isoformat(),
        "session_end": None,
        "model": model,
        "total_messages": 0,
        "user_info": {}
    }

    try:
        while True:
            user_input = input(f"\n{Fore.GREEN}Escribe tu pregunta: {Style.RESET_ALL}")
            if user_input.lower() == 'exit':
                metadata["session_end"] = datetime.now().isoformat()
                print(f"\n{Fore.YELLOW}¡Hasta luego! 👋{Style.RESET_ALL}")
                break
            response = invoke_function(user_input, history)
            if history is not None:
                history.append(HumanMessage(content=user_input))
                history.append(response)
                metadata["total_messages"] += 2
            print(f"\n{Fore.BLUE}Lukita 🤖: {Style.RESET_ALL}{response.content}")
    except Exception as e:
        metadata["session_end"] = datetime.now().isoformat()
        raise e
    finally:
        if history and len(history) > 0 and should_save:
            if chat_metadata:
                metadata.update(chat_metadata)
            save_conversation(history, metadata)

    return metadata