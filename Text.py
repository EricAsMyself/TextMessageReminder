
def main():
    people = get_people()
    send_message(people)


def get_people():
    return ['jacob', 'isaac']

def send_message(people):
    for person in people:
        print("sending the message: " + person)
        message = client.messages.create(
            body="REMINDER" + message,
            from_="+16802034912",
            to=PHONE_NUMBER
        )

if __name__ == "__main__":
    main()