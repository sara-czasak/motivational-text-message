# Motivational Text Message 💬

A simple Python script that sends a random motivational quote to your phone twice a day via SMS.

## How it works

- Fetches a random quote from the [API Ninjas Quotes API](https://api-ninjas.com/api/quotes)
- Sends it to your phone using [Twilio](https://www.twilio.com/)
- Runs automatically every day at 6am and 8pm via GitHub Actions

## Setup

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with the following variables:
   TWILIO_ACCOUNT_SID=your_sid
   TWILIO_AUTH_TOKEN=your_token
   TWILIO_NUMBER=your_twilio_number
   MY_NUMBER=your_phone_number
   API_NINJAS_KEY=your_api_key
4. Run `python main.py`
