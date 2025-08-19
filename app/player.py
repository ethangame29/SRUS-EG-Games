
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

    def set_name(self, name):
        self.__name = name

    @classmethod
    def hash_function(cls, key: str) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total

    def __hash__(self):
        return self.hash_function(self.uid)