from agent import SimpleAIAgent

def main():
    agent = SimpleAIAgent()
    print("Simple AI Agent: Hi! Type something to talk to me. Type 'bye' to exit.") 

# Here is function

    while True: 
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Simple AI Agent:", agent.respond(user_input)) 
            break
        else: 
            print("Simple AI Agent:", agent.respond(user_input))  


if __name__ == "__main__":
    main() 
