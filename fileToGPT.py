import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# Read the contents of the text file
with open('input.txt', 'r') as file:
    text = file.read()

with open('input.txt', 'a') as file:
    additional_text = "\n\n\nsolve the conflict above and summrise the convestion"
    file.write(additional_text)

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

slack_token = "xoxb-5245319467909-5245510607157-FmgnMSyxya2AeAP1tMcPisa8"
client = WebClient(token=slack_token)

channel_id = "C0577A24AF7"  # The ID of the Slack channel you want to send the message to

# Send the message to Slack
try:
    generated_response = message.json()['choices'][0]['message']['content']
    response = client.chat_postMessage(channel=channel_id, text=generated_response)
    print("Message sent successfully!")
except SlackApiError as e:
    print(f"Error sending message to Slack: {e.response['error']}")