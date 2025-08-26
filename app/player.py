
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
