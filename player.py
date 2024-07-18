import random

class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 5
        self.debt = 0
        self.position = 0  # Start position

    def update_balance(self, amount):
        self.balance += amount
        if self.balance < 0:
            self.debt += abs(self.balance)
            self.balance = 0

    def roll_dice(self, consecutive_rolls=0):
        if consecutive_rolls > 5:
            print(f"{self.name} rolled 'RollAgain' more than 5 times consecutively. Stopping dice roll.")
            return "RollAgainLimitExceeded"
        
        dice_outcomes = [1, 2, 3, "RollAgain"]
        outcome = random.choices(dice_outcomes, weights=[0.4, 0.2, 0.2, 0.2], k=1)[0]

        if outcome == "RollAgain":
            print(f"{self.name} rolled 'RollAgain'. Rolling again...")
            return self.roll_dice(consecutive_rolls + 1)

        return outcome


    def move(self, steps):
        self.position = (self.position + steps - 1) % 12 + 1

    def take_loan(self, amount):
        if amount <= 10 * self.balance and self.balance > 0:
            self.update_balance(amount)
            self.debt += amount  # Update balance based on loan taken
            print(f"{self.name} took a loan of {amount}.")
        else:
            print(f"{self.name} cannot take a loan greater than 10 times their balance or if balance is not positive.")

    def repay_loan(self, amount):
        if amount <= self.balance and amount <= self.debt:
            self.update_balance(-amount)  # Update balance based on loan repayment
            self.debt -= amount
            print(f"{self.name} repaid a loan of {amount}.")
        else:
            print(f"{self.name} cannot repay more than their balance or the debt amount.")

    def apply_board_effect(self, board, other_player=None):
        square_type = board.board_layout[(self.position - 1) // 4][(self.position - 1) % 4]

        if square_type == 'B':
            self.update_balance(10)  # Gain 10 units from Bank
            print(f"{self.name} gained 10 units from the Bank.")
            action = input(f"{self.name}, do you want to Take a loan (Y/N):  ").upper()
            if action == "Y":
                loan_amount = int(input(f"Enter loan amount (max 10 times balance: {10 * self.balance}): "))
                self.take_loan(loan_amount)
            elif action == "N":
                action = input(f"{self.name}, do you want to Repay a loan (Y/N):  ").upper()
                if action == "Y":
                    repay_amount = int(input(f"Enter repay amount (max debt: {self.debt}): "))
                    self.repay_loan(repay_amount)
        
        elif square_type == 'J':
            self.update_balance(-20)  # Lose 20 units for Jail
            print(f"{self.name} lost 20 units and misses the next turn due to Jail.")
        
        elif square_type == 'H':
            if self.balance > 0:
                self.update_balance(2)  # Gain 2 units from House if balance is positive
            elif self.balance < 0:
                self.update_balance(-2)  # Lose 2 units from House if balance is negative
            if self.debt > 0:
                self.debt += 1  # Increase debt by 1 if there is debt
            print(f"{self.name} landed on a House.")
            if other_player and other_player.position == self.position:
                half_balance = (other_player.balance + 1) // 2
                self.update_balance(half_balance)  # Gain half of opponent's balance from House
                other_player.update_balance(-half_balance)  # Decrease opponent's balance accordingly
                print(f"{self.name} received {half_balance} units from {other_player.name}'s House.")

        else:
            print(f"{self.name} landed on a neutral square.")

