from app.player_list import PlayerList
from app.player import Player


class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message


def player_locator(player_list, key):

    current_node = None

    if player_list.head is not None:
        current_node = player_list.head
        id = current_node.key
        while id is not key:
            current_node = current_node.prev_node
            id = current_node.key

    return current_node


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = []
        for number in range(self.SIZE):
            self.hashmap.append(PlayerList())

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash_function(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:
        player_list = self.hashmap[self.get_index(key)]
        player = player_locator(player_list, key)

        if player is None:
            player_list.append(key, name)
        else:
            player.player.name = name

    def __getitem__(self, key: str):
        player_list = self.hashmap[self.get_index(key)]
        player = player_locator(player_list, key)

        if player is not None:
            return player.player
        else:
            raise NotFoundError("Player not found")

    def __delitem__(self, key: str):
        player_list = self.hashmap[self.get_index(key)]
        player = player_locator(player_list, key)

        if player is not None:
            player_list.pop(key)
        else:
            raise NotFoundError("Player not found")

    def __len__(self):
        length = 0
        for player_list in self.hashmap:
            length = length + len(player_list)
        return length
