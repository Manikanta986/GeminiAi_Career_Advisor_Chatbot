from backend.gemini_client import get_ai_response
from backend.prompt_manager import PromptManager
from backend.memory_manager import MemoryManager
from backend.logger import log_info, log_error

memory = MemoryManager()

def ask_chatbot(user_input):

    try:
        memory.add_user_message(user_input)

        prompt = PromptManager.build_prompt(user_input, memory.get_history())

        response = get_ai_response(prompt)

        memory.add_bot_message(response)

        log_info(f"User: {user_input}")
        log_info(f"Bot: {response}")

        return response

    except Exception as e:
        log_error(str(e))
        return "Something went wrong. Try again."