import random

class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 5
        self.debt = 0
        self.position = 0  # Start position

    def update_balance(self, amount):
        self.balance += amount

    def roll_dice(self, consecutive_rolls=0):
        if consecutive_rolls > 5:
            print(f"{self.name} rolled 'RollAgain' more than 5 times consecutively. Stopping dice roll.")
            return "RollAgainLimitExceeded"
        
        dice_outcomes = [1, 2, 3, "RollAgain"]
        try:
            outcome = random.choices(dice_outcomes, weights=[0.4, 0.2, 0.2, 0.2], k=1)[0]
        except IndexError:
            print("Error: Unable to choose dice outcome.")
            return None

        if outcome == "RollAgain":
            print(f"{self.name} rolled 'RollAgain'. Rolling again...")
            return self.roll_dice(consecutive_rolls + 1)

        return outcome


    def move(self, steps):
        try:
            self.position = (self.position + steps - 1) % 12 + 1
        except TypeError:
            print("Error: Unable to move player due to invalid steps value.")

    def take_loan(self, amount):
        try:
            if amount <= 10 * self.balance and self.balance > 0:
                self.update_balance(amount)
                self.debt += amount
                print(f"{self.name} took a loan of {amount}.")
            else:
                print(f"{self.name} cannot take a loan greater than 10 times their balance or if balance is not positive.")
        except TypeError:
            print("Error: Unable to process loan due to invalid amount.")

    def repay_loan(self, amount):
        try:
            if amount <= self.balance and amount <= self.debt:
                self.update_balance(-amount)
                self.debt -= amount
                print(f"{self.name} repaid a loan of {amount}.")
            else:
                print(f"{self.name} cannot repay more than their balance or the debt amount.")
        except TypeError:
            print("Error: Unable to process loan repayment due to invalid amount.")

    def apply_board_effect(self, board, other_player=None):
        try:
            square_type = board.board_layout[(self.position - 1) // 4][(self.position - 1) % 4]

            if square_type == 'B':
                self.update_balance(10)
                print(f"{self.name} gained 10 units from the Bank.")
                action = input(f"{self.name}, do you want to Take a loan (Y/N):  ").upper()
                if action == "Y":
                    try:
                        loan_amount = int(input(f"Enter loan amount (max 10 times balance: {10 * self.balance}): "))
                        self.take_loan(loan_amount)
                    except ValueError:
                        print("Error: Invalid input for loan amount.")
                elif action == "N":
                    action = input(f"{self.name}, do you want to Repay a loan (Y/N):  ").upper()
                    if action == "Y":
                        try:
                            repay_amount = int(input(f"Enter repay amount (max debt: {self.debt}): "))
                            self.repay_loan(repay_amount)
                        except ValueError:
                            print("Error: Invalid input for repayment amount.")

            elif square_type == 'J':
                self.update_balance(-20)
                print(f"{self.name} lost 20 units and misses the next turn due to Jail.")
            
            elif square_type == 'H':
                if self.balance > 0:
                    self.update_balance(2)
                elif self.balance < 0:
                    self.update_balance(-2)
                if self.debt > 0:
                    self.debt += 1
                print(f"{self.name} landed on a House.")
                if other_player and other_player.position == self.position:
                    half_balance = (other_player.balance + 1) // 2
                    self.update_balance(half_balance)
                    other_player.update_balance(-half_balance)
                    print(f"{self.name} received {half_balance} units from {other_player.name}'s House.")

            else:
                print(f"{self.name} landed on a neutral square.")

        except IndexError:
            print("Error: Unable to apply board effect due to invalid board layout indices.")
        except ValueError:
            print("Error: Unable to apply board effect due to invalid input.")

