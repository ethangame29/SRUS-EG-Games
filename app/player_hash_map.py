from app.player_list import PlayerList
from app.player import Player


class NotFoundError(Exception):
    """
    Throws NotFoundError.

    Args:
        message (str): Error Message.

    Returns:
        None
    """
    def __init__(self, message):
        self.message = message


def player_locator(player_list, key):
    """
    Locates a Player in a HashMap.

    Args:
        player_list (PlayerList): The Player List.
        key (str): Player Key.

    Returns:
        None or current_node
    """
    current_node = None

    if player_list.head is not None:
        current_node = player_list.head
        while current_node is not None and current_node.key is not key:
            current_node = current_node.prev_node

    if current_node is not None and current_node.key == key:
        return current_node
    else:
        return None


class PlayerHashMap:
    """
    Hash Map for storing Players
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
        Gets index of a Player through a hash.

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
        Set a player in Hash Map.

        Args:
            key (str): The player key.
            name (str): The player name.
        """
        player_list = self.hashmap[self.get_index(key)]
        player = player_locator(player_list, key)

        if player is None:
            player_list.append(key, name)
        else:
            player.player.name = name

    def __getitem__(self, key: str):
        """
        Get Player from Hash Map.

        Args:
            key (str): The player key.

        Returns:
            player
        """
        player_list = self.hashmap[self.get_index(key)]
        player = player_locator(player_list, key)

        if player is not None:
            return player.player
        else:
            raise NotFoundError("Player not found")

    def __delitem__(self, key: str):
        """
        Deletes Player from Hash Map.

        Args:
            key (str): The Player Key
        """
        player_list = self.hashmap[self.get_index(key)]
        player = player_locator(player_list, key)

        if player is not None:
            player_list.pop(key)
        else:
            raise NotFoundError("Player not found")

    def __len__(self):
        """
        Grabs Length of Hash Map

        returns:
            int: length
        """
        length = 0
        for player_list in self.hashmap:
            length = length + len(player_list)
        return length
