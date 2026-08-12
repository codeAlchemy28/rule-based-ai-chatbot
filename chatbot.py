#Project-1
print("Welcome to DecodeBot!")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print()
while True:
    u_input=input("You: ")
    u_input=u_input.lower().strip()
    u_input=u_input.rstrip("?!.,:;").strip()
    if u_input=="bye" or u_input=="exit" or u_input=="quit":
        print("Bot: Goodbye! Have a great day!")
        break
    elif u_input=="hello":
        print("Bot: Hello! How can I help you?")
    elif u_input=="hi":
        print("Bot: Hi there! Nice to meet you.")
    elif u_input=="hey":
        print("Bot: Hey! What's up?")
    elif u_input=="good morning":
        print("Bot: Good morning! Have a wonderful day!")
    elif u_input=="good evening":
        print("Bot: Good evening! How can I help you?")
    elif u_input=="how are you":
        print("Bot: I'm doing great! Thanks for asking.")
    elif u_input=="what is your name":
        print("Bot: I'm DecodeBot, a rule-based AI chatbot.")
    elif u_input=="who are you":
        print("Bot: I'm DecodeBot! I respond using predefined rules.")
    elif u_input=="what can you do":
        print("Bot: I can respond to greetings and simple questions.")
    elif u_input=="thank you" or u_input=="thanks":
        print("Bot: You're welcome!")
    else:
        print("Bot: Sorry, I don't understand that yet.")
