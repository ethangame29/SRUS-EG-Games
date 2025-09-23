import unittest
from app.player_bst import PlayerBST
from app.player import Player

class PlayerBSTTest(unittest.TestCase):

    def test_bst_insert_empty(self):
        player = Player(1,"Ethan")
        bst = PlayerBST()
        bst.insert(player)
        self.assertEqual(bst.root.player.name, "Ethan")

    def test_bst_insert_with_root(self):
        player = Player(1, "Ethan")
        player2 = Player(2, "Jeb")
        player3 = Player(3, "Bill")
        bst = PlayerBST()
        bst.insert(player)
        bst.insert(player2)
        bst.insert(player3)
        self.assertEqual(bst.root.player.name, "Ethan")
        self.assertEqual(bst.root.left.player.name, "Bill")
        self.assertEqual(bst.root.right.player.name, "Jeb")

    def test_bst_insert_with_sub_branches(self):
        player = Player(1, "E")
        player2 = Player(2, "G")
        player3 = Player(3, "D")

        player4 = Player(4, "B")
        player5 = Player(5, "H")
        player6 = Player(6, "F")
        player7 = Player(7, "A")
        player8 = Player(8, "C")

        bst = PlayerBST()

        bst.insert(player)
        bst.insert(player2)
        bst.insert(player3)
        bst.insert(player4)
        bst.insert(player5)
        bst.insert(player6)
        bst.insert(player7)
        bst.insert(player8)

        # First Branch and Root
        self.assertEqual(bst.root.player.name, "E")
        self.assertEqual(bst.root.left.player.name, "D")
        self.assertEqual(bst.root.right.player.name, "G")
        # Left Side
        self.assertEqual(bst.root.left.left.player.name, "B")
        self.assertEqual(bst.root.left.left.left.player.name, "A")
        self.assertEqual(bst.root.left.left.right.player.name, "C")
        # Right Side
        self.assertEqual(bst.root.right.right.player.name, "H")
        self.assertEqual(bst.root.right.left.player.name, "F")

if __name__ == '__main__':
    unittest.main()