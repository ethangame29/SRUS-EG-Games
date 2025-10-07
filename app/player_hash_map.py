from app.player_list import PlayerList
from app.player import Player


class PlayerHashMap:
    """
    Hash Map for storing Players. Holds a number of player_list which each will contain the players.
    """
    SIZE: int = 10

    def __init__(self):
        self.hashmap = []
        for number in range(self.SIZE):
            self.hashmap.append(PlayerList())

    def display(self):
        """
        Displays the Hash Map in console
        """
        index = 0
        for player_list in self.hashmap:
            if len(player_list) >= 1:
                print(f"List {index}")
                player_list.display()
                print("\n")
            index += 1

    def get_index(self, key: str | Player) -> int:
        """
        Gets player_list index through a hashing a player key.

        Args:
            key (str | Player): The player key.

        Returns:
            int: Hash Value
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.hash_function(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:
        """
        Add/Set a player in Hash Map. The player_list is located by hashing the key.
        It will either set or override if the player exists in the list or not.

        Args:
            key (str): The player key.
            name (str): The player name.
        """
        player_list = self.hashmap[self.get_index(key)]

        try:
            player = PlayerList.player_locator(player_list, key)
            player.player.name = name
        except KeyError:
            player_list.append(key, name)

    def __getitem__(self, key: str):
        """
        Get Player from Hash Map. The player_list is located by hashing the key.

        Args:
            key (str): The player key.

        Returns:
            player
        """
        player_list = self.hashmap[self.get_index(key)]
        player = PlayerList.player_locator(player_list, key)

        return player.player

    def __delitem__(self, key: str):
        """
        Pops player from a hashmap. The player_list is located by hashing the key.

        Args:
            key (str): The Player Key
        """
        player_list = self.hashmap[self.get_index(key)]
        return player_list.pop(key)

    def __len__(self):
        """
        Counts the number of players in a hashmap and returns the total.

        returns:
            int: length
        """
        length = 0
        for player_list in self.hashmap:
            length = length + len(player_list)
        return length
