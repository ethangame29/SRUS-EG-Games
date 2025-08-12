import player_node
import player

class PlayerList:

    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def append(self, id, name):
        if self.__head is not None:
            newNode = player_node.PlayerNode(player.Player(id, name))
            self.__head.setNextNode(newNode)
            newNode.setPrevNode(self.__head)
            self.__head = newNode
        else:
            newNode = player_node.PlayerNode(player.Player(id, name))
            self.__head = newNode
            self.__tail = newNode

    def appendEnd(self, id, name):
        if self.__head is not None:
            newNode = player_node.PlayerNode(player.Player(id, name))
            self.__tail.setPrevNode(newNode)
            newNode.setNextNode(self.__tail)
            self.__tail = newNode
        else:
            self.append(id, name)
