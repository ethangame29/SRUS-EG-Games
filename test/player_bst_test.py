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

    #           E
    #          / \
    #         D   G
    #        /   / \
    #       B   F   H
    #      / \
    #     A   C

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

    def test_bst_search(self):
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

        found_player1 = bst.search("E")
        found_player2 = bst.search("G")
        found_player3 = bst.search("D")
        found_player4 = bst.search("B")
        found_player5 = bst.search("H")
        found_player6 = bst.search("F")
        found_player7 = bst.search("A")
        found_player8 = bst.search("C")

        self.assertEqual(found_player1.name, "E")
        self.assertEqual(found_player2.name, "G")
        self.assertEqual(found_player3.name, "D")
        self.assertEqual(found_player4.name, "B")
        self.assertEqual(found_player5.name, "H")
        self.assertEqual(found_player6.name, "F")
        self.assertEqual(found_player7.name, "A")
        self.assertEqual(found_player8.name, "C")

    def test_create_sorted_list(self):
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

        correct_list = [player, player2, player3, player4, player5, player6, player7, player8]

        sorted = bst.create_sorted_list()

        self.assertEqual(sorted, correct_list)

    # Balanced Tree
    #            E
    #          /   \
    #         C     G
    #        / \   / \
    #       B   D F   H
    #      /
    #     A

    def test_optimise_bst(self):
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

        bst.optimise()

        # First Branch and Root
        self.assertEqual(bst.root.player.name, "E")
        self.assertEqual(bst.root.left.player.name, "C")
        self.assertEqual(bst.root.right.player.name, "G")
        # Left Side
        self.assertEqual(bst.root.left.left.player.name, "B")
        self.assertEqual(bst.root.left.left.left.player.name, "A")
        self.assertEqual(bst.root.left.right.player.name, "D")
        # Right Side
        self.assertEqual(bst.root.right.right.player.name, "H")
        self.assertEqual(bst.root.right.left.player.name, "F")

if __name__ == '__main__':
    unittest.main()