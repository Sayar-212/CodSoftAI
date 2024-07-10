import re
import random
import getpass
from datetime import datetime
#dataset
patterns_responses = {
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey!'],
    r'okay|great|thanks': ['Its my pleasure', 'Honoured to help you', 'Elementary from my side. Ask more'],
    r'how are you\??': ['I am fine, thank you! What about you?', 'Doing well, what about you?'],
    r'i am sad\??': ['Oh no! Forget it. Wanna hear a joke?', 'Wanna hear a joke? It will make you smile.'],
    r'what is your name\??': [ 'Hi, I am Sherlock!','You can call me mine!. Just kidding, I am Sherlock.'],
    r'bye|goodbye|byeee': ['Good Bye?! Itni Jaldi?','Abhi na jao chhodkar :('],
    r'what can you do\??': ['I can chat with you and answer simple questions.', 'I can help you with basic information and tasks.'],
    r'what is the weather like\??': ['I am not sure about the weather right now, but you can check a weather website.', 'I don’t have real-time weather data, but I can chat with you!'],
    r'tell me a joke|another joke|one more': ['Why don’t scientists trust atoms? Because they make up everything!', 'Why did the scarecrow win an award? Because he was outstanding in his field!', 'Why is the obtuse triangle always so frustrated? Because it’s never right.'],
    r'hahaha': ['Hehe, it was nice to know I added some laughter in your life! Feel free to interact.'],
    r'do you have any hobbies\??': ['I enjoy chatting with people like you!', 'I love learning new things and helping users.'],
    r'who created you\??': ['I was created by Sayar Basu, Codsoft AI Intern', 'I was created by AI intern at Codsoft, Sayar Basu'],
    r'can you help me\??': ['I will do my best to help you.', 'Sure, let me know what you need help with.'],
    r'what is your favorite color\??': ['I like the color blue.', 'Red is a nice color!'],
    r'generate|create': ['I am not GPT. I am a rules-based chatbot. Write "menu" to know my capabilities'],
    r'what are you doing\??': ['Smoking a cigar. Wanna have a sniff? Carry on with your query'],
}
#dynamic response data set
dynamic_responses = {
    r'(.) your name(.)': ['My name is Sherlock.', 'You can call me mine!. Just kidding, I am Sherlock.'],
    r'(.) you do(.)': ['I can chat with you and help you with information.', 'I can assist you with simple tasks.'],
    r'(.) created you(.)': ['I was created by a team of AI enthusiasts.', 'A group of developers created me.'],
}
def get_dynamic_response(user_input):
    for pattern, responses in dynamic_responses.items():
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            return random.choice(responses)
    return None
def get_response(user_input, context):
    user_input = user_input.lower()
    if context['expecting_joke_response']:
        if 'yes' in user_input:
            context['expecting_joke_response'] = False
            return random.choice(patterns_responses[r'tell me a joke|another joke|one more'])
        else:
            context['expecting_joke_response'] = False
            return "Alright, let me know if you change your mind!"
    if 'how old are you' in user_input:
        return "I am 170 yrs old, but I'm here to help you like a teenager!"
    elif 'what time is it' in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"It's {current_time} right now in the system. For accuracy, check your clock."
    elif 'what is the capital of india' in user_input:
        return "The capital of India is New Delhi."
    elif 'what is the largest country by area' in user_input:
        return "The largest country by area is Russia."
    elif 'who was albert einstein' in user_input:
        return "Albert Einstein was a theoretical physicist who developed the theory of relativity."
    elif 'how many bones are in the human body' in user_input:
        return "An adult human has 206 bones."
    elif 'what is the largest planet in our solar system' in user_input:
        return "The largest planet in our solar system is Jupiter."
    elif 'when did world war ii end' in user_input:
        return "World War II ended in 1945."
    elif 'who invented the telephone' in user_input:
        return "The telephone was invented by Alexander Graham Bell."
    elif 'who wrote pride and prejudice' in user_input:
        return "Pride and Prejudice was written by Jane Austen."
    elif 'menu' in user_input:
        return "\nCommands I can handle:\n- How are you?\n- What time is it?\n- What is the capital of India?\n- What is the largest country by area?\n- Who was Albert Einstein?\n- How many bones are in the human body?\n- What is the largest planet in our solar system?\n- When did World War II end?\n- Who invented the telephone?\n- Who wrote Pride and Prejudice?\n- Tell me a joke\n- Do you have any hobbies?\n- Who created you?\n- Can you help me?\n- What is your favorite color?\n\nFeel free to ask!"
    else:
        for pattern, responses in patterns_responses.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                response = random.choice(responses)
                if 'joke' in response.lower():
                    context['expecting_joke_response'] = True
                return response
        dynamic_response = get_dynamic_response(user_input)
        if dynamic_response:
            return dynamic_response
        if context['last_question'] == 'how are you?':
            context['last_question'] = ''
            return "I'm glad to hear that! How can I assist you today?"
        return "I didn't study that. Beyond my Rules/data."
def greet_user():
    username = getpass.getuser()
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return f"{greeting}, {username}. I am Sherlock, how can I help you?"
def chatbot_interaction():
    context = {'last_question': '', 'expecting_joke_response': False}
    print(greet_user())
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Sherlock: Fine, Goodbye mate!")
            break
        response = get_response(user_input, context)
        print(f"Sherlock: {response}")
        if 'how are you' in user_input.lower():
            context['last_question'] = 'how are you?'
chatbot_interaction()
