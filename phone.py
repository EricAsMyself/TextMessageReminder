from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
class Texting:
    def __init__(self):
        self.client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))
    
    def send_message(self, message):
        self.client.messages.create(
            body=message,
            from_=os.getenv('FROM_PHONE_NUMBER'),
            to=os.getenv('PHONE_NUMBER')
        )

