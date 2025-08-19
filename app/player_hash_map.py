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
        playerFound = False
        playerList = self.hashmap[self.get_index(key)]
        currentNode = playerList.head
        while currentNode is not None:
            if currentNode.player.uid == key:
                currentNode.player.set_name(name)
                playerFound = True
            currentNode = currentNode.prevNode

        if not playerFound:
            playerList.append(key, name)
