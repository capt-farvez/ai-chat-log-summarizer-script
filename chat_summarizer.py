import os
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

CHAT_LOG_PATH = './chat.txt'  # Default chat log path, can be changed as needed.

def parse_chat_log(file_path=CHAT_LOG_PATH):
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_log = file.readlines()

    user_messages = []
    ai_messages = []

    for line in chat_log:
        if line.startswith("User:"):
            user_messages.append(line[5:].strip()) # Remove "User: " prefix
        elif line.startswith("AI:"):
            ai_messages.append(line[3:].strip()) # Remove "AI: " prefix

    return user_messages, ai_messages


if __name__ == "__main__":
    if os.path.exists(CHAT_LOG_PATH):
        user_messages = parse_chat_log(CHAT_LOG_PATH)[0]
        ai_messages = parse_chat_log(CHAT_LOG_PATH)[1]
        print(f"Total messages: {len(user_messages) + len(ai_messages)}")
        print(f"User messages: {len(user_messages)}")
        print(f"AI messages: {len(ai_messages)}")
        print("\nUser Messages:")
        for msg in user_messages:
            print(f"- {msg}")
        print("\nAI Messages:")
        for msg in ai_messages:
            print(f"- {msg}")
    else:
        print("Error: File not found. Make sure chat.txt is in the same directory.")
