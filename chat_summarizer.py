import os
import nltk
from nltk.corpus import stopwords
import re
from collections import Counter

# Ensure stopwords are downloaded
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

CHAT_LOG_PATH = './chat.txt'  # Default chat log path, can be changed as needed.
CHAT_LOG_FOLDER_PATH = './chat_logs'  # Default folder for multiple chat logs

def parse_chat_log(file_path):
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

def get_keywords(messages):
    all_text = ' '.join(messages).lower()
    words = re.findall(r"\b\w+\b", all_text)
    # Remove stopwords 
    filtered_words = []
    for word in words:
        if word in STOPWORDS:
            continue
        else:
            filtered_words.append(word)
    # Count word frequencies
    keyword_counts = Counter(filtered_words)
    return keyword_counts.most_common(5)

def summarize_chat(file_path):
    user_messages = parse_chat_log(file_path)[0]
    ai_messages = parse_chat_log(file_path)[1]

    user_messages_count = len(user_messages)
    ai_messages_count = len(ai_messages)
    total_messages = user_messages_count + ai_messages_count
    keywords = get_keywords(user_messages + ai_messages)

    print("Chat Summary:")
    print(f"- The conversation had {total_messages} exchanges. Where User sent {user_messages_count} messages and AI sent {ai_messages_count} messages.")
    print(f"- The user asked mainly about {keywords[0][0]} and {keywords[1][0]}.")
    print(f"- Most common keywords:", ', '.join([f"{word[0]}" for word in keywords]) , ".")

def summarize_all_chats(folder_path):
    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            print(f"\n{i+1}. Summarizing of chat log file: {filename}")
            summarize_chat(os.path.join(folder_path, filename))

if __name__ == "__main__":
    # uncomment the following lines to summarize a single chat log
    # if os.path.exists(CHAT_LOG_PATH):
    #     summarize_chat(CHAT_LOG_PATH)
    # else:
    #     print("Error: File not found. Make sure chat.txt is in the same directory.")

    if os.path.exists(CHAT_LOG_FOLDER_PATH):
        summarize_all_chats(CHAT_LOG_FOLDER_PATH)
    else:
        print("Error: Folder not found. Make sure the folder path is correct.")