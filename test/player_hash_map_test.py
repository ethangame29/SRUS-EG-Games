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

    def test_hash_map_set(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("1", "Ethan")
        hash_map.__setitem__("3", "Bob")
        hash_map.__setitem__("2", "Bill")
        hash_map.__setitem__("8", "Jeb")
        self.assertEqual(hash_map.__getitem__("1").uid, "1")
        self.assertEqual(hash_map.__getitem__("3").uid, "3")
        self.assertEqual(hash_map.__getitem__("2").uid, "2")
        self.assertEqual(hash_map.__getitem__("8").uid, "8")

    def test_hash_map_get_index(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("1", "Ethan")
        hash_map.__setitem__("3", "Bob")
        hash_map.__setitem__("2", "Bill")
        hash_map.__setitem__("12", "Jeb")
        index = hash_map.get_index("1")
        self.assertEqual(index, 9)

    def test_hash_map_get(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("1", "Ethan")
        hash_map.__setitem__("3", "Bob")
        hash_map.__setitem__("2", "Bill")
        hash_map.__setitem__("8", "Jeb")
        player = hash_map.__getitem__("3")
        self.assertEqual(int(player.uid), 3)

    def test_hash_map_remove(self):
        hash_map = PlayerHashMap()
        hash_map.__setitem__("1", "Bob")
        hash_map.__setitem__("12", "Bill")
        hash_map.__delitem__("12")
        with self.assertRaises(Exception):
            hash_map.__getitem__("12")


if __name__ == '__main__':
    unittest.main()
