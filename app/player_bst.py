from player_bnode import PlayerBNode


class PlayerBST:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player, location = None):
        if self._root is None:
            self._root = PlayerBNode(player)
            return

        if location is None:
            location = self._root
            # return

        if location.player.name > player.name:
            if location.left is None:
                location.left = PlayerBNode(player)
            else:
                self.insert(player, location.left)
        else:
            if location.right is None:
                location.right = PlayerBNode(player)
            else:
                self.insert(player, location.right)

    def search(self, name: str, location = None):
        if self._root is None:
            return

        if location is None:
            location = self._root

        if location.player.name == name:
            return location.player

        if location.player.name > name:
            return self.search(name, location.left)
        else:
            return self.search(name, location.right)

    def optimise(self):
        sorted = self.create_sorted_list()
        self._root = None
        self.rebalance_tree(sorted)

    def rebalance_tree(self, array):
        if len(array) <= 1:
            if len(array) == 1:
                self.insert(array[0])
            return array

        pivot = array.pop(len(array) // 2)
        self.insert(pivot)

        left = []
        right = []
        for player in array:
            if player.name < pivot.name:
                left.append(player)
            else:
                right.append(player)
        return self.rebalance_tree(left) + [pivot] + self.rebalance_tree(right)

    def create_sorted_list(self, location = None, players = None):
        if players is None:
            players = [self.root.player]
        if location is None:
            location = self.root

        if location.left is not None and location.right is not None:
            return self.create_sorted_list(location.left, [location.left.player]) + players + self.create_sorted_list(location.right, [location.right.player])
        elif location.left is not None:
            return self.create_sorted_list(location.left, [location.left.player]) + players
        elif location.right is not None:
            return players + self.create_sorted_list(location.right, [location.right.player])
        else:
            return players