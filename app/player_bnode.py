class PlayerBNode:

    def __init__(self, player):
        self._player = player
        self._left = None
        self._right = None

    def __repr__(self):
        return f"({self._player.name} <<{self._left}<< || >>{self._right}>>)"

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return  self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
