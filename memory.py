class Memory:
    def __init__(self):
        self.history = []

    def add_interaction(self, user_input, response):
        self.history.append((user_input, response)) 
  
    def get_history(self):
        return self.history
    def clear_memory(self):  
        self.history = [] 