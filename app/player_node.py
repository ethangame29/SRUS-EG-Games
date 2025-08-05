
class PlayerNode:

    def __init__(self, player):
        self.__player = player
        self.__nextNode = None
        self.__prevNode = None

    def __str__(self):
        return f"{self.__nextNode}\n[{self.__player}]\n{self.__prevNode}"

    @property
    def player(self):
        return self.__player

    @property
    def key(self):
        return self.__player.uid

    @property
    def nextNode(self):
        return self.nextNode

    @property
    def prevNode(self):
        return self.__prevNode