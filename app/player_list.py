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

    def display(self, forward = True):
        if forward is True:
            currentNode = self.__head
            while currentNode is not None:
                print(currentNode.player)
                currentNode = currentNode.prevNode
        else:
            currentNode = self.__tail
            while currentNode is not None:
                print(currentNode.player)
                currentNode = currentNode.nextNode

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

    def popHead(self):
        self.__head = self.__head.prevNode
        self.__head.setNextNode = None

    def popTail(self):
        self.__tail = self.__tail.nextNode
        self.__tail.setPrevNode = None

    def pop(self, key):
        id = self.__head.key
        currentNode = self.__head
        while id is not key:
            currentNode = currentNode.prevNode
            id = currentNode.key
        prevnode = currentNode.prevNode
        nextnode = currentNode.nextNode

        nextnode.setPrevNode(prevnode)
        prevnode.setNextNode(nextnode)

        return id