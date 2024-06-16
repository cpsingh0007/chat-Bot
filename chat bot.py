from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi there! How can I help?"]
    ],
    [
        r"(.*) your name?",
        ["I am a chatbot created in Python.", "I'm a Python-powered chatbot."]
    ],
    [
        r"(.*) created you?",
        ["I was created using Python.", "Python is my creator."]
    ],
    [
        r"quit",
        ["Bye!", "It was nice talking to you. See you soon!"]
    ],
]

def chatbot():
    print("Hi, I'm the chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
