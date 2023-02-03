# Text Message Reminder
## Introduction

This project utilizes the Twilio API to send out text messages to a group of people as a reminder.
Requirements

* Twilio account and API credentials
* Python 3.6 or higher
* Twilio Python library
* A list of phone numbers to send messages to

## Installation

1. Install the Twilio library by running pip install twilio
1. Create a .env file in the root directory of the project and add the following environment variables:
    TWILIO_ACCOUNT_SID - Your Twilio Account SID
    TWILIO_AUTH_TOKEN - Your Twilio Auth Token
    TWILIO_PHONE_NUMBER - The phone number provided by Twilio to send messages from
1. Create a sql server
## Usage

4. Run python send_reminder.py
1. Enter the message you would like to send as the reminder
1. The script will send the message to all phone numbers listed in the sql server.

## Note

Please make sure to use valid phone numbers and test sending a message to yourself before sending to a group to avoid any mistake.