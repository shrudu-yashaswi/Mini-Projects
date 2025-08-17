print("NEW")
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I’m just a program, but I’m doing great! Thanks for asking."
    elif "your name" in user_input:
        return "I’m a simple AI Chatbot created by you!"
    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines."
    elif "joke" in user_input:
        return "Why don’t scientists trust atoms? Because they make up everything! 😄"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I don't understand that yet, but I'm learning!"

print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("AI Chatbot:", response)
    if "bye" in user_message.lower():
        break