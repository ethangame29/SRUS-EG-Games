
class PlayerNode:

    def __init__(self, player):
        self._player = player
        self._nextNode = None
        self._prevNode = None

    def __str__(self):
        return f"{self._nextNode}\n[{self._player}]\n{self._prevNode}"

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self._player.uid

    @property
    def next_node(self):
        return self._nextNode

    @next_node.setter
    def next_node(self, node):
        self._nextNode = node

    @property
    def prev_node(self):
        return self._prevNode

    @prev_node.setter
    def prev_node(self, node):
        self._prevNode = node
