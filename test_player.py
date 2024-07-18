import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player = Player("TestPlayer")

    def test_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.balance, 5)
        self.assertEqual(self.player.debt, 0)
        self.assertEqual(self.player.position, 0)

    def test_update_balance(self):
        self.player.update_balance(10)
        self.assertEqual(self.player.balance, 15)
        self.assertEqual(self.player.debt, 0)

        self.player.update_balance(-20)
        self.assertEqual(self.player.balance, 0)
        self.assertEqual(self.player.debt, 5)

    def test_roll_dice(self):
        outcome = self.player.roll_dice()
        self.assertIn(outcome, [1, 2, 3, "RollAgainLimitExceeded"])

    # Add more tests for other methods as needed

if __name__ == "__main__":
    unittest.main()
