import requests
import os
import dotenv


dotenv.load_dotenv()
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
MY_NUMBER = os.getenv("MY_NUMBER")