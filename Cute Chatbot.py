#Chatbot 
from datetime import datetime

print("𝜗ৎ ChatPy: Hiii~ I’m ChatPy! Your tiny code bestie 🐥")
print("You can say things like 'hi', 'how are you', 'time', or 'bye' to chat with me!\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatPy: Hiii cutie! 🎧ྀི♪⋆.✮ How can I brighten your day? 𐙚⋆°｡⋆♡")

    elif user_input in ["how are you", "how are you?"]:
        print("ChatPy: I’m feeling ★ code-tastic ★ today! What about you? ★")

    elif "your name" in user_input:
        print("ChatPy: I’m ChatPy! Just a little bot made with love 💕 and Python ꫂ ၴႅၴ")

    elif "time" in user_input:
        now = datetime.now()
        print(f"ChatPy: It's currently ✩°｡🧸𓏲⋆.🧺𖦹 ₊˚ {now.strftime('%H:%M')} — time flies when we’re chatting! 🕊️")

    elif "date" in user_input:
        today = datetime.today()
        print(f"ChatPy: Today’s date is 📅 {today.strftime('%Y-%m-%d')} — another day to shine! 🌟")

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("ChatPy: Aww okay ✩°｡🧸𓏲⋆.🧺𖦹 ₊˚ Chat again soon, bestie! Stay safe and hydrated 🫧𓇼𓏲*ੈ✩‧₊˚🎐 Byeee~ 👋🐣")
        break

    else:
        print("ChatPy: Oopsie! I didn’t quite get that 🐾 Can you try saying it another way? 🧐")

