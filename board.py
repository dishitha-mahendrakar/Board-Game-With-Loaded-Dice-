import random

class Board:
    def __init__(self, squares):
        self.squares = squares

    def roll_dice(self):
        roll = random.choices([1, 2, 3, 'RollAgain'], [0.4, 0.2, 0.2, 0.2])[0]
        while roll == 'RollAgain':
            roll = random.choices([1, 2, 3, 'RollAgain'], [0.4, 0.2, 0.2, 0.2])[0]
        return roll
