import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertEqual(len(self.board.board_layout), 4)
        self.assertEqual(len(self.board.positions), 4)

    def test_display_board(self):
        self.board.display_board([])

if __name__ == "__main__":
    unittest.main()
