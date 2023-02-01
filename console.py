from phone import Texting
from SQLDB import Database
import logging
import os
from dotenv import load_dotenv






def main():
    logging.info("Initializing the program")
    people_db = Database()
    phone = Texting()


    # logging.info("Adding People")
    # people_db.add_person("Eric", "Poole", os.getenv('PHONE_NUMBER'))
    # people_db.add_person("John", "Doe", os.getenv('PHONE_NUMBER'))

    logging.info("Getting People")
    result = people_db.get_people()
    message = create_message()
    text_people(phone, result, message)




def text_people(phone: Texting, people, message):
    logging.info("starting to text People")
    y_n = input(f"do you want to send out \"{message}\"?")
    if y_n == "y":
        logging.info("User Ok message")
        print("Sending...")
        people_texted = ""
        for person in people:
            named_message = message.replace("*f*", person[1]).replace("*l*", person[2])
            print(named_message)
            phone.send_message(named_message, person[3])
            people_texted += f"{str(person[2])} \n"
        phone.send_message(f"We sent a message out to:\n{people_texted}" ,os.getenv('PHONE_NUMBER'))
    else:
        print('Not sending...')
        logging.info("USER DENIED MESSAGE")

def create_message():
    message = input("""Please write out a message *f* or *l* with spaces before and after if you want Their name to be shown:""")
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