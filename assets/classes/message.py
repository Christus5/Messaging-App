from abc import ABCMeta, abstractmethod
from random import randint, choice
from time import asctime
from assets.data_base import (users, messages)


class AbstractMessage(metaclass=ABCMeta):
    @abstractmethod
    def check_self(self):
        pass

    @abstractmethod
    def generate_message(self):
        pass

    @abstractmethod
    def to_html(self):
        pass


class Message(AbstractMessage):
    def __init__(self, content: str = '', sender: str = '', date='',
                 rtime: float = 0.0, is_user: bool = False):
        self.__content = content
        self.__sender = sender
        self.date = date

        # float returned form time.time() method for comparint to current time
        self.rtime = rtime

        self.check_self()
        self.is_user = is_user

    def check_self(self):
        if not self.__content and \
                not self.__sender and \
                not self.date:
            self.generate_message()

    def generate_message(self):
        text = []
        for _ in range(randint(1, 100)):
            text.append(chr(randint(97, 122)))

        self.__content = ''.join(text)
        existing_users = list(users.find())
        self.__sender = "Server" if not existing_users else choice(existing_users)['username']
        self.date = asctime()

    def to_html(self):
        div_style = 'margin-top: 10px;'
        date_style = 'color: gray; font-size: 8pt;'
        sender_style = 'color: blue;'

        if self.is_user:
            sender_style = 'color: red;'

        return f'''<div style="{div_style}"> 
                        <span style="{sender_style}">{self.__sender}</span>: {self.__content}
                        <br/>
                        <span style="{date_style}"><em>{self.date}</em></span>
                    </div>'''

    def append_to_mongodb(self):
        message = {
            'message': self.__content,
            'sender': self.__sender,
            'date': self.date,
            'rtime': self.rtime
        }

        messages.insert_one(message)

    def __str__(self):
        return f"{self.__sender}: {self.__content}"
