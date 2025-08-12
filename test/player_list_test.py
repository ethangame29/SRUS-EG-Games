import unittest
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_append_to_empty_list(self):
        playerList = PlayerList()
        playerList.append(1234, "Joe")
        self.assertEqual(playerList.head.key, 1234)
        self.assertEqual(playerList.head, playerList.tail)

    def test_append_to_non_empty_list(self):
        playerList = PlayerList()
        playerList.append(1234, "Joe")
        self.assertEqual(playerList.head.key, 1234)
        playerList.append(3, "Ethan")
        self.assertEqual(playerList.head.key, 3)
        self.assertEqual(playerList.head.prevNode.key, 1234)
        self.assertEqual(playerList.head.prevNode.nextNode.key, 3)
        self.assertEqual(playerList.head.prevNode, playerList.tail)

    def test_append_to_end_of_list(self):
        playerlist = PlayerList()
        playerlist.appendEnd(1234, "Joe")
        self.assertEqual(playerlist.tail.key, 1234)
        playerlist.appendEnd(3, "Ethan")
        self.assertEqual(playerlist.tail.key, 3)
        self.assertEqual(playerlist.head.key, 1234)
        self.assertEqual(playerlist.head.prevNode, playerlist.tail)
        self.assertEqual(playerlist.tail.nextNode, playerlist.head)

    def test_pop_head(self):
        playerlist = PlayerList()
        playerlist.append(1234, "Joe")
        playerlist.append(3, "Ethan")
        playerlist.append(1, "Bob")
        playerlist.popHead()
        self.assertEqual(playerlist.head.key, 3)

    def test_pop_tail(self):
        playerlist = PlayerList()
        playerlist.append(1234, "Joe")
        playerlist.append(3, "Ethan")
        playerlist.append(1, "Bob")
        playerlist.popTail()
        self.assertEqual(playerlist.tail.key, 3)

    def test_pop_by_key(self):
        playerlist = PlayerList()
        playerlist.append(1234, "Joe")
        playerlist.append(3, "Ethan")
        playerlist.append(1, "Bob")
        self.assertEqual(playerlist.pop(3), 3)
        self.assertEqual(playerlist.head.prevNode, playerlist.tail)
        self.assertEqual(playerlist.tail.nextNode, playerlist.head)
