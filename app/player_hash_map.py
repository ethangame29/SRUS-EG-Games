from app.player_list import PlayerList
from app.player import Player

class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message

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
        player_found = False
        player_list = self.hashmap[self.get_index(key)]
        current_node = player_list.head
        while current_node is not None:
            if current_node.player.uid == key:
                current_node.player.set_name(name)
                player_found = True
            current_node = current_node.prevNode

        if not player_found:
            player_list.append(key, name)

    def __getitem__(self, key: str) -> None:
        player_found = False
        player_list = self.hashmap[self.get_index(key)]
        current_node = player_list.head
        while current_node is not None:
            if current_node.player.uid == key:
                player_found = True
            current_node = current_node.prevNode

        if player_found:
            return current_node.player
        else:
            raise NotFoundError("Player not found")

    def __delitem__(self, key: str):
        player_found = False
        player_list = self.hashmap[self.get_index(key)]
        current_node = player_list.head
        while current_node is not None:
            if current_node.player.uid == key:
                player_found = True
            current_node = current_node.prevNode

        if player_found:
            player_list.pop(key)
        else:
            raise NotFoundError("Player not found")
