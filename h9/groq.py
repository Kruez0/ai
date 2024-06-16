import os
from groq import Groq

client = Groq(
api_key="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"
)

def get_chat_completion(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def chat():
    print("Enter message ('quit' to exit):")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            print("Bye!")
            break
        response = get_chat_completion(user_input)
        print(response)

if __name__ == "__main__":
    chat()
