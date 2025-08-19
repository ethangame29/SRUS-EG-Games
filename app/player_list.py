import player_node
import player

class PlayerList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def __len__(self):
        return self.__length

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
        self.__length += 1

    def appendEnd(self, id, name):
        if self.__head is not None:
            newNode = player_node.PlayerNode(player.Player(id, name))
            self.__tail.setPrevNode(newNode)
            newNode.setNextNode(self.__tail)
            self.__tail = newNode
        else:
            self.append(id, name)
        self.__length += 1

    def popHead(self):
        self.__head = self.__head.prevNode
        self.__head.setNextNode = None
        self.__length -= 1
    def popTail(self):
        self.__tail = self.__tail.nextNode
        self.__tail.setPrevNode = None
        self.__length -= 1

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

        self.__length -= 1

        return id