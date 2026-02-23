from memory import Memory
from utils import Utils

class SimpleAIAgent:
    def __init__(self):
        self.memory = Memory() 
        self.utils = Utils()
        self.responses = {
            "hello": "Hello! How can I help you?",
            "how are you": "I'm just a program, but I'm doing great! How about you?", 
            
            "what's your name": "I'm a simple AI agent.", 
            "bye": "Goodbye! Have a great day!",
            "tell me a joke": self.utils.tell_joke,
            "calculate": lambda expr: self.utils.calculate(expr), 
            "history": lambda: "\n".join([f"You: {i[0]}\nAgent: {i[1]}" for i in self.memory.get_history()]),
            "clear memory": self.memory.clear_memory,
            "default": "I'm not sure how to respond to that."
        }
  
    def respond(self, user_input):
        user_input = user_input.lower().strip()
        response = self.responses.get(user_input, self.responses["default"])

        # Handle special cases
        if user_input.startswith("calculate"):
            expr = user_input.replace("calculate", "").strip()
            response = self.responses["calculate"](expr)
        elif user_input == "history":
            response = self.responses["history"]()
        elif user_input == "clear memory":
            response = "Memory cleared!"
            self.responses["clear memory"]()

        # Add interaction to memory
        self.memory.add_interaction(user_input, response)
        return response
