from assets.classes.message import Message
from threading import Thread


def create_message():
    message = Message()
    message.append_to_mongodb()


def generate_messages(quantity: int):
    if quantity > 100:
        for _ in range(quantity):
            t = Thread(target=create_message)
            t.start()
            t.join()
    else:
        for _ in range(quantity):
            create_message()
