import requests
import os
import dotenv
from twilio.rest import Client


dotenv.load_dotenv()
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
MY_NUMBER = os.getenv("MY_NUMBER")
API_NINJAS_KEY = os.getenv("API_NINJAS_KEY")
QUOTE_ENDPOINT = 'https://api.api-ninjas.com/v2/randomquotes'

headers = {
    'X-Api-Key': API_NINJAS_KEY,
}

params = {
    'categories': 'inspirational',

}

response = requests.get(QUOTE_ENDPOINT, headers=headers, params=params)
data = response.json()
quote = data[0]['quote']
author = data[0]['author']

message_text = f"\n\nToday's motivational quote is:\n {quote}\n\t-{author}"
print(message_text)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body=message_text,
    from_=TWILIO_NUMBER,
    to=MY_NUMBER,
)