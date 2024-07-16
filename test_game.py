import unittest
from player import Player
from board import Board
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.board = Board("HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH")
        self.game = Game(self.player1, self.player2, self.board)

    def test_initial_balance(self):
        self.assertEqual(self.player1.balance, 5)
        self.assertEqual(self.player1.debt, 0)
        self.assertEqual(self.player2.balance, 5)
        self.assertEqual(self.player2.debt, 0)

    def test_roll_dice(self):
        roll = self.board.roll_dice()
        self.assertIn(roll, [1, 2, 3])

    def test_move_player(self):
        self.player1.move(3, self.board)
        self.assertEqual(self.player1.position, 3)
        self.assertEqual(self.player1.balance, -15)  # After landing on Jail
        self.assertTrue(self.player1.miss_next_turn)

    def test_game_winner(self):
        self.player1.balance = 200
        self.assertTrue(self.game.check_winner())
        self.player1.balance = 5
        self.player2.debt = 200
        self.assertTrue(self.game.check_winner())

if __name__ == '__main__':
    unittest.main()
