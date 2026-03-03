import abc


class Client(abc.ABC):
    def __init__(self, client):
        self.__client = client

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    def __getattr__(self, name):
        if hasattr(self.__client, name):
            return getattr(self.__client, name)
