import unittest
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_append_to_empty_list(self):
        playerList = PlayerList()
        playerList.append(1234, "Joe")
        self.assertEqual(playerList.head.key, 1234)

    def test_append_to_non_empty_list(self):
        playerList = PlayerList()
        playerList.append(1234, "Joe")
        self.assertEqual(playerList.head.key, 1234)
        playerList.append(3, "Ethan")
        self.assertEqual(playerList.head.key, 3)
        self.assertEqual(playerList.head.prevNode.key, 1234)
        self.assertEqual(playerList.head.prevNode.nextNode.key, 3)