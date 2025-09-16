import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):

    def test_player_name_return(self):
        a = Player(1234, "Joe")
        self.assertEqual(a.name, "Joe")

    def test_player_id_return(self):
        a = Player(1234, "Joe")
        self.assertEqual(a.uid, 1234)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(1, "Alice", score=10)
        bob = Player(2, "Bob", score=5)

        # Add the appropriate expression to the following assert test
        #self.assertTrue()
        # or, event better
        self.assertLess(bob, alice)

    def test_sort_players(self):
        alice = Player(1, "Alice", score=10)
        bob = Player(2, "Bob", score=5)
        charlie = Player(3, "Charlie",  score=15)

        players = [alice, bob, charlie]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        alice1 = Player(1, "Alice", score=10)
        bob1 = Player(2, "Bob", score=5)
        charlie1 = Player(3, "Charlie", score=15)
        manually_sorted_players = [bob1, alice1, charlie1]
        
        self.assertListEqual(sorted_players, manually_sorted_players)
