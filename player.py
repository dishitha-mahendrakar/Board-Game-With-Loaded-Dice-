class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 5
        self.debt = 0
        self.position = 0
        self.miss_next_turn = False

    def display_status(self):
        print(f"{self.name}'s Balance: {self.balance}, Debt: {self.debt}, Position: {self.position}")

    def move(self, steps, board):
        self.position = (self.position + steps) % len(board.squares)
        self.apply_square_effect(board)

    def apply_square_effect(self, board):
        square = board.squares[self.position]
        if square == 'B':
            self.balance += 10
            print(f"{self.name} landed on a Bank. Balance increased to {self.balance}")
            # Loan or repayment options could be added here
        elif square == 'J':
            self.balance -= 20
            self.miss_next_turn = True
            print(f"{self.name} landed in Jail. Balance decreased to {self.balance} and misses next turn.")
        elif square == 'H':
            if self.balance > 0:
                self.balance += 2
            else:
                self.balance -= 2
            if self.debt > 0:
                self.debt += 1
            print(f"{self.name} landed on a House. Balance is now {self.balance}, Debt is now {self.debt}")

