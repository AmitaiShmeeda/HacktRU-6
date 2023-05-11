
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize a Slack API client with your app token
client = WebClient(token='xoxb-5245319467909-5245510607157-FmgnMSyxya2AeAP1tMcPisa8')

# Specify the channel or conversation ID for which you want to extract the chat transcript
channel_id = 'C0577A24AF7'

# Make the API call to retrieve the conversation history
try:
    response = client.conversations_history(channel=channel_id)
    messages = response['messages']
    # Process the messages or save them to a file
    for message in messages:
        print(message['text'])
except SlackApiError as e:
    print(f"Error retrieving conversation history: {e.response['error']}")
