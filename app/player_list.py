import player_node
import player


class PlayerList:

    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def display(self, forward=True):
        if forward is True:
            current_node = self._head
            while current_node is not None:
                print(current_node.player)
                current_node = current_node.prev_node
        else:
            current_node = self._tail
            while current_node is not None:
                print(current_node.player)
                current_node = current_node.next_node

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

    def append_end(self, id, name):
        if self._head is not None:
            new_node = player_node.PlayerNode(player.Player(id, name))
            self._tail.prev_node = new_node
            new_node.next_node = self._tail
            self._tail = new_node
        else:
            self.append(id, name)

    def pop_head(self):
        id = self._head.key
        self._head = self._head.prev_node
        if self._head is not None:
            self._head.next_node = None
        return id

    def pop_tail(self):
        id = self._tail.key
        self._tail = self._tail.next_node
        if self._tail is not None:
            self._tail.prev_node = None
        return id

    def pop(self, key):
        id = self._head.key
        current_node = self._head
        while id is not key:
            current_node = current_node.prev_node
            id = current_node.key

        if self._head == current_node:
            id = self.pop_head()
        elif self._tail == current_node:
            id = self.pop_tail()
        else:
            prev_node = current_node.prev_node
            next_node = current_node.next_node

            current_node.prev_node = None
            current_node.next_node = None

            if prev_node is not None and next_node is not None:
                next_node.prev_node = prev_node
                prev_node.next_node = next_node

        return id
