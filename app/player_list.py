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
        return self._length

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
        self._length += 1

    def append_end(self, id, name):
        if self._head is not None:
            new_node = player_node.PlayerNode(player.Player(id, name))
            self._tail.prev_node = new_node
            new_node.next_node = self._tail
            self._tail = new_node
        else:
            self.append(id, name)
        self._length += 1

    def player_locator(self, key):
        """
        Iterates through a player_list until provided key matches and then returns.

        Args:
            self (PlayerList): The Player List.
            key (str): Player Key.

        Returns:
            current_node
        """
        current_node = None

        if self.head is not None:
            current_node = self.head
            while current_node is not None and current_node.key is not key:
                current_node = current_node.prev_node

        if current_node is not None and current_node.key == key:
            return current_node
        else:
            raise KeyError("Player not found")

    def pop_head(self):
        id = self._head.key
        self._head = self._head.prev_node
        if self._head is not None:
            self._head.next_node = None
        self._length -= 1
        return id

    def pop_tail(self):
        id = self._tail.key
        self._tail = self._tail.next_node
        if self._tail is not None:
            self._tail.prev_node = None
        self._length -= 1
        return id

    def pop(self, key):
        """
        Calls player_locator to then find and pop a player by the given key.

        Args:
            key (str): Player Key.

        Returns:
        player id
        """
        player = self.player_locator(key)

        if self._head == player:
            id_ = self.pop_head()
        elif self._tail == player:
            id_ = self.pop_tail()
        else:
            prev_node = player.prev_node
            next_node = player.next_node

            player.prev_node = None
            player.next_node = None

            next_node.prev_node = prev_node
            prev_node.next_node = next_node

            id_ = player.key

            self._length -= 1

        return id_
