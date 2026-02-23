class MemoryManager:

    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append(f"User: {message}")

    def add_bot_message(self, message):
        self.history.append(f"Bot: {message}")

    def get_history(self):
        return self.history