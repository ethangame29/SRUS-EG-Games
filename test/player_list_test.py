import unittest
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_append_to_empty_list(self):
        player_list = PlayerList()
        player_list.append(1234, "Joe")
        self.assertEqual(player_list.head.key, 1234)
        self.assertEqual(player_list.head, player_list.tail)

    def test_append_to_non_empty_list(self):
        player_list = PlayerList()
        player_list.append(1234, "Joe")
        self.assertEqual(player_list.head.key, 1234)
        player_list.append(3, "Ethan")
        self.assertEqual(player_list.head.key, 3)
        self.assertEqual(player_list.head.prev_node.key, 1234)
        self.assertEqual(player_list.head.prev_node.next_node.key, 3)
        self.assertEqual(player_list.head.prev_node, player_list.tail)

    def test_append_to_end_of_list(self):
        player_list = PlayerList()
        player_list.append_end(1234, "Joe")
        self.assertEqual(player_list.tail.key, 1234)
        player_list.append_end(3, "Ethan")
        self.assertEqual(player_list.tail.key, 3)
        self.assertEqual(player_list.head.key, 1234)
        self.assertEqual(player_list.head.prev_node, player_list.tail)
        self.assertEqual(player_list.tail.next_node, player_list.head)

    def test_pop_head(self):
        player_list = PlayerList()
        player_list.append(1234, "Joe")
        player_list.append(3, "Ethan")
        player_list.append(1, "Bob")
        player_list.pop_head()
        self.assertEqual(player_list.head.key, 3)

    def test_pop_tail(self):
        player_list = PlayerList()
        player_list.append(1234, "Joe")
        player_list.append(3, "Ethan")
        player_list.append(1, "Bob")
        player_list.pop_tail()
        self.assertEqual(player_list.tail.key, 3)

    def test_pop_by_key(self):
        player_list = PlayerList()
        player_list.append(1234, "Joe")
        player_list.append(3, "Ethan")
        player_list.append(1, "Bob")
        self.assertEqual(player_list.pop(3), 3)
        self.assertEqual(player_list.head.prev_node, player_list.tail)
        self.assertEqual(player_list.tail.next_node, player_list.head)
