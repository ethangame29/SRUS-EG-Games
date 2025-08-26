import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):

    def test_player_name_return(self):
        a = Player(1234, "Joe")
        self.assertEqual(a.name, "Joe")

    def test_player_id_return(self):
        a = Player(1234, "Joe")
        self.assertEqual(a.uid, 1234)
