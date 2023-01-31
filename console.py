from phone import Texting
from SQLDB import Database

# TODO remove this!
import os
from dotenv import load_dotenv

load_dotenv() # This loads in the environmental variables.


def main():
    people_db = Database()
    phone = Texting()

    people_db.add_person("Eric", "Poole", os.getenv('PHONE_NUMBER'))

    result = people_db.get_people()

    text_people(phone, result, "Welcome to the ward")



def text_people(phone: Texting, people, message):
    try:
        people_texted = ""
        for person in people:
            phone.send_message(message, person[3])
            people_texted += str(person[2])
        phone.send_message(f"We sent a message out to: {people_texted}" ,os.getenv('PHONE_NUMBER'))
    except Exception as e:
        print(e)
        message(phone, f"Error sending text messages {e}" ,os.getenv('PHONE_NUMBER'))



def add_people(db :Database, fname, lname, phone):
    db.add_person(fname,lname, phone) 
    print("done getting people")

def message(phone : Texting, message, phone_number):
    phone.send_message(message, phone_number)

if __name__ == "__main__":
    main()