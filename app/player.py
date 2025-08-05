
class Player:

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def __str__(self):
        return f"{self.__name} | ID: {self.__id}"

    @property
    def uid(self):
        return self.__id

    @property
    def name(self):
        return self.__name