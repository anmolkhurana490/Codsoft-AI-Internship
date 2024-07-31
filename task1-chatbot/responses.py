response_data={
    # Greetings
    ("hello", "hi", "hey"): "Hello! How can I assist you today?",
    ("goodbye", "bye", "see you"): "Goodbye! Have a great day!",

    # General Questions
    ("how are you?", "how's it going?"): "I'm just a bot, but I'm doing great! How about you?",
    ("what is your name?", "who are you?"): "I'm a simple rule-based chatbot created to assist you.",
    ("what can you do?", "what are your capabilities?"): "I can chat with you, answer your questions, and assist with basic tasks.",

    # Informational Questions
    ("what is the weather like?", "how is the weather?"): "I can't check the weather, but it's always sunny in the world of bots!",
    ("what time is it?", "current time"): "I don't have access to the current time, but you can check your device's clock.",
    ("what day is it?", "what's the date today?"): "I don't have access to today's date, but you can check your device's calendar.",

    # Small Talk
    ("tell me a joke"): "Why don't scientists trust atoms? Because they make up everything!",
    ("tell me a fun fact"): "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.",
    ("what is your favorite color?"): "As a bot, I don't have preferences, but I like all colors equally!",

    # Assistance
    ("help", "assistance"): "Sure! What do you need help with?",
    ("how do I reset my password?", "forgot password"): "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions to reset it.",
    ("how do I contact support?", "customer support"): "You can contact our support team by emailing support@example.com or calling 123-456-7890.",

    # Feedback
    ("thank you", "thanks"): "You're welcome! If you have any more questions, feel free to ask.",
    ("you're great", "good job"): "Thank you! I'm here to help you.",

    # Common Misunderstanding
    ("not understandable"): "I'm sorry, I don't understand that. Could you please rephrase?"
}

def get_response(prompt):
    promt=prompt.lower()
    prompt_lists=response_data.keys()
    for prompt_list in prompt_lists:
        if(prompt in prompt_list):
            return response_data[prompt_list]
    else:
        return response_data["not understandable"]
    
if __name__=="__main__":
    while(True):
        user_input=input("--> ")
        if(user_input=="exit"):
            break
        bot_response=get_response(user_input)
        print("Bot:", bot_response)
