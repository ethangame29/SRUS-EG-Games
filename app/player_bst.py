from player_bnode import PlayerBNode


class PlayerBST:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player, location):
        if self._root is None:
            self._root = PlayerBNode(player)
            return

        if location is None:
            location = self._root
            # return

        if location.player.name < player.name:
            if location.left is None:
                location.left = PlayerBNode(player)
            else:
                self.insert(player, location.left)
        else:
            if location.right is None:
                location.right = PlayerBNode(player)
            else:
                self.insert(player, location.right)
