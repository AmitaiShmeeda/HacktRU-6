# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:33:35 2023

@author: shira
"""

import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

Slack_API = 'xoxb-5245319467909-5245510607157-oslajGIWC78eyejqJ9ZJTWmH'
# Define the channel, group, or direct message ID
channel_id = 'C057ED09JSE'

# Initialize the Slack API client
client = WebClient(token=Slack_API)

# Set the file path to save the chat messages
file_path = 'chat_log.txt'

# Retrieve the chat history
response = client.conversations_history(channel=channel_id)

if response["ok"]:
    messages = response["messages"]

    # Iterate through each message and append the text to the file
    with open(file_path, 'a') as file:
        for message in messages:
            if 'text' in message:
                text = message['text']
                file.write(text + '\n')
else:
    print("Error occurred while retrieving chat history:", response["error"])

# solve the conflict above and summrize the convestion
question = "find if there is misinformation in the given text\n\n\n"
# Read the contents of the text file
with open('chat_log.txt', 'r') as file:
    text = file.read()

text = question + text

# Prepare the API request
headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': text}]
}

# Send the API request
message = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

slack_token = Slack_API
client = WebClient(token=slack_token)

# Send the message to Slack
try:
    generated_response = message.json()['choices'][0]['message']['content']
    response = client.chat_postMessage(channel=channel_id, text=generated_response)
    print("Message sent successfully!")
except SlackApiError as e:
    print(f"Error sending message to Slack: {e.response['error']}")
    
# clean the chat_log file
# file_path = 'chat_log.txt'
# with open(file_path, 'w') as file:
#     file.write('')  # Write an empty string to clear the file
# file.close()
    