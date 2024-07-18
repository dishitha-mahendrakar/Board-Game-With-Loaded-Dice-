import unittest
from unittest.mock import patch
from io import StringIO
import sys
from main import *

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=["Player1", "Player2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_play(self, mock_stdout, mock_input):
        try:
            game_play()
            self.assertIn("wins", mock_stdout.getvalue())
        except KeyboardInterrupt:
            self.fail("Game exited with KeyboardInterrupt")

    # Add more tests for other methods as needed

if __name__ == "__main__":
    unittest.main()
