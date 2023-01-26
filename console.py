from phone import Texting
from SQLDB import Database


def main():
    message("")


def message(message):
    phone = Texting()
    phone.send_message("hello world")

if __name__ == "__main__":
    main()