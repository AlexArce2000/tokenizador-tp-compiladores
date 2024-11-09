from transformers import pipeline

# Cargar el modelo de conversación
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Interactuar en la terminal
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    response = chatbot(user_input)
    print("Bot:", response[-1]['generated_text'])
