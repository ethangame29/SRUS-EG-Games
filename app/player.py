
class Player:

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __str__(self):
        return f"{self._name} | ID: {self._id}"

    @property
    def uid(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def hash_function(cls, key: str) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total

    def __hash__(self):
        return self.hash_function(self.uid)
