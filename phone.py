from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv() # This loads in the environmental variables.
class Texting:
    def __init__(self):
        self.client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN')) # This takes in the
        # Tokens and produces a client which can send out messages.
    

    # This will send a message out. When you have initialized the class, and add a message.
    def send_message(self, message, phone_number):
        self.client.messages.create(
            body=message,
            from_=os.getenv('FROM_PHONE_NUMBER'),
            to=phone_number
        )

