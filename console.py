from phone import Texting
import sqlite3


def main():
    message(sqlite3.version)


def message(message):
    print(message)
    # phone = Texting()
    # phone.send_message("hello world")

if __name__ == "__main__":
    main()