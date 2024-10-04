import google.generativeai as genai

def chat_system():
    print("Welcome to the system. Say 'bye' to exit. \n")
    
  
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"}
        ]
    )
    
    while True:
        text = input("You: ").strip() 
        if text.lower() == "bye":
            print("AI: B bye! Have a good day!")
            break 
            
        response = chat.send_message(text)
        print("AI:", response.text) 


chat_system()
