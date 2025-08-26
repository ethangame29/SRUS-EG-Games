import player_node
import player


class PlayerList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __len__(self):
        return self.__length

    def display(self, forward= rue):

        if forward is True:
            current_node = self._head
            while current_node is not None:
                print(current_node.player)
                current_node = current_node.prevNode
        else:
            current_node = self._tail
            while current_node is not None:
                print(current_node.player)
                current_node = current_node.nextNode

    def append(self, id, name):
        if self._head is not None:
            new_node = player_node.PlayerNode(player.Player(id, name))
            self._head.next_node = new_node
            new_node.prev_node = self._head
            self._head = new_node
        else:
            new_node = player_node.PlayerNode(player.Player(id, name))
            self._head = new_node
            self._tail = new_node
        self._length += 1

    def append_end(self, id, name):
        if self._head is not None:
            new_node = player_node.PlayerNode(player.Player(id, name))
            self._tail.prev_node = new_node
            new_node.next_node = self._tail
            self._tail = new_node
        else:
            self.append(id, name)
        self.__length += 1

    def pop_head(self):
        self._head = self._head.prev_node
        self._head.next_node = None
        self._length -= 1
    def pop_tail(self):
        self._tail = self._tail.next_node
        self._tail.prev_node = None
        self._length -= 1

    def pop(self, key):
        id = self._head.key
        current_node = self._head
        while id is not key:
            current_node = current_node.prev_node
            id = current_node.key
        prev_node = current_node.prev_node
        next_node = current_node.next_node

        next_node.prev_node = prev_node
        prev_node.next_node = next_node

        self._length -= 1

        return id
