import unittest
from board import Board
from player import Player

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertIsInstance(self.board.board_layout, list)
        self.assertIsInstance(self.board.positions, list)

    def test_display_board(self):
        # Mock players
        player1 = Player("Player1")
        player2 = Player("Player2")
        player1.position = 1
        player2.position = 2

        with self.assertRaises(Exception):
            self.board.display_board([player1, player2])

        # Add more tests for other methods as needed

if __name__ == "__main__":
    unittest.main()
