import unittest
from game import Game
from player import Player
from board import Board

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Player1", "Player2")

    def test_initialization(self):
        self.assertIsInstance(self.game.board, Board)
        self.assertIsInstance(self.game.player1, Player)
        self.assertIsInstance(self.game.player2, Player)
        self.assertEqual(self.game.current_player, self.game.player1)

    def test_switch_player(self):
        initial_player = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(self.game.current_player, initial_player)

    def test_check_and_print_win_conditions(self):
        self.game.player1.balance = 150
        self.assertTrue(self.game.check_and_print_win_conditions())

if __name__ == "__main__":
    unittest.main()
