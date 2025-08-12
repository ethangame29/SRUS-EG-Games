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
