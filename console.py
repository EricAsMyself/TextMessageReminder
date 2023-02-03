from phone import Texting
from SQLDB import Database
import logging
import os
from dotenv import load_dotenv
import pandas as pd
from tqdm import tqdm


# The main function calls out each of the othr functions and classes, to send out texts
def main():
    logging.info("Initializing the program")
    people_db = Database()
    phone = Texting()

    add_from_csv(people_db, r'families.csv')

    logging.info("Getting People")
    result = people_db.get_people()
    message = create_message()
    text_people(phone, result, message)



 # This will take in the database, path and if the information is not added twice, then it will
 # add the names and phone number to the database.
def add_from_csv(db :Database, path):
    logging.info("added people to database")

    df = pd.read_csv(path).values

    logging.info("Imported dataframe.")
    for person in df:
        if not db.check_person(person[0], person[1]):
            db.add_person(person[0], person[1], person[2])


# Here is where the magic happens. THis takes in people and message and texts out to each person.
def text_people(phone: Texting, people, message):
    logging.info("starting to text People")
    y_n = input(f"do you want to send out \"{message}\"?") # Checks to see if you want to send.
    if y_n == "y":
        logging.info("User Ok message")
        people_texted = ""
        for person in tqdm(people): # Loops through people and replaces words with names.
            named_message = message.replace("*f*", person[1]).replace("*l*", person[2])
            logging.info(named_message)
            phone.send_message(named_message, person[3])
            people_texted += f"{str(person[2])} \n"
            # Sends a text out to the admin to show that all people have recieved the text.
        phone.send_message(f"We sent a message out to:\n{people_texted}" ,os.getenv('PHONE_NUMBER'))
        logging.info(f"We sent a message out to:\n{people_texted}")
    else: # loggs error.
        logging.info('Not sending...')
        logging.info("USER DENIED MESSAGE")

def create_message():
    message = input("Please write out a message *f* or *l* with spaces before and after if you want Their name to be shown:")
    return message

if __name__ == "__main__":
    load_dotenv() # This loads in the environmental variables.
    # This sets up the logging format
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename='TextMessageReminder.log',
                        filemode='w')
    main()