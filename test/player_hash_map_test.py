import unittest
from app.player_hash_map import PlayerHashMap


class PlayerHashMapTest(unittest.TestCase):

    def test_hash_map_len(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("1", "Ethan")
        hash_map.__setitem__("3", "Bob")
        hash_map.__setitem__("2", "Bill")
        hash_map.__setitem__("8", "Jeb")
        self.assertEqual(len(hash_map), 4)

    def test_hash_map_get_index(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("1", "Ethan")
        hash_map.__setitem__("3", "Bob")
        hash_map.__setitem__("2", "Bill")
        hash_map.__setitem__("8", "Jeb")
        index = hash_map.get_index("1")
        self.assertEqual(index, 9)

    def test_hash_map_get(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("3", "Ethan")
        player = hash_map.__getitem__("3")
        self.assertEqual(int(player.uid), 3)

    def test_hash_map_remove(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("3", "Ethan")
        hash_map.__delitem__("3")
        player = hash_map.__getitem__("3")
        self.assertEqual(int(player.uid), 3)


if __name__ == '__main__':
    unittest.main()
