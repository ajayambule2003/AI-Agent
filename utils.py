import random

class Utils:
    @staticmethod
    def calculate(expression):
        try:
            return str(eval(expression))
        except:  
            return "Sorry, I couldn't calculate that."  

    @staticmethod
    def tell_joke():  
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
        ]
        return random.choice(jokes)
