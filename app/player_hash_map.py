from app.player_list import PlayerList
from app.player import Player

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
        playerList = self.hashmap[self.get_index(key)]
        current_node = playerList.head
        while current_node is not None:
            if current_node.player.uid == key:
                current_node.player.set_name(name)
                player_found = True
            current_node = current_node.prevNode

        if not player_found:
            playerList.append(key, name)
