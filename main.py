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
quote = response.json()[0]['quote']
author = response.json()[0]['author']

message_text = f"Today's motivational quote is:\n {quote}\n\t-{author}"
print(message_text)
