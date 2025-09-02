
class PlayerNode:

    def __init__(self, player):
        self._player = player
        self._next_node = None
        self._prev_node = None

    def __str__(self):
        return f"{self._next_node}\n[{self._player}]\n{self._prev_node}"

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self._player.uid

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, node):
        self._prev_node = node
