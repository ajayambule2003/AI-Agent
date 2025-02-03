## main.py (Entry Point)
from agent import AIAgent

def main():
    agent = AIAgent()
    print("AI Agent is ready. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break  
        response = agent.get_response(user_input)
        print("AI: ", response)

if __name__ == "__main__":
    main()

## agent.py (Core AI Logic)
from responses import get_predefined_response
from utils import preprocess_input

class AIAgent:
    def __init__(self):
        print("Initializing AI Agent...")
    
    def get_response(self, user_input):
        processed_input = preprocess_input(user_input)
        response = get_predefined_response(processed_input)
        return response

## responses.py (Predefined Responses)
def get_predefined_response(input_text):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a program, but I'm doing great!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(input_text, "I'm not sure how to respond to that.")

## utils.py (Utility Functions)
def preprocess_input(text):
    return text.lower().strip()

## config.py (Configuration Settings)
BOT_NAME = "Simple AI Agent"

## requirements.txt (Dependencies)
# No dependencies required for now, but you can list future ones here.
