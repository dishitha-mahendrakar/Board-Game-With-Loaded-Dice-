from player import Player
from board import Board
import random

class Game:
    def __init__(self, player1_name, player2_name):
        try:
            self.board = Board()
            self.player1 = Player(player1_name)
            self.player2 = Player(player2_name)
            self.current_player = self.player1
        except ValueError:
            print("Error: Unable to initialize game due to invalid player names.")

    def switch_player(self):
        try:
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        except TypeError:
            print("Error: Unable to switch players due to invalid current player.")

    def check_and_print_win_conditions(self):
        try:
            self.opponent_player = self.player1 if self.current_player == self.player2 else self.player2

            current_player_balance_check = self.current_player.balance - self.current_player.debt
            current_player_debt_check = self.current_player.debt - self.current_player.balance
            opponent_player_balance_check = self.opponent_player.balance - self.opponent_player.debt
            opponent_player_debt_check = self.opponent_player.debt - self.opponent_player.balance
            
            if current_player_balance_check > 100:
                print(f"{self.current_player.name} wins because {self.current_player.name}'s (Balance - Debt) = {current_player_balance_check} which is > 100!")
                return True
            elif current_player_debt_check > 100:
                print(f"{self.opponent_player.name} wins because {self.current_player.name}'s (Debt - Balance) = {current_player_debt_check} which is > 100!")
                return True
            elif opponent_player_balance_check > 100:
                print(f"{self.opponent_player.name} wins because {self.opponent_player.name}'s (Balance - Debt) = {opponent_player_balance_check} which is > 100")
                return True
            elif opponent_player_debt_check > 100:
                print(f"{self.current_player.name} wins because {self.opponent_player.name}'s (Debt - Balance) = {opponent_player_debt_check} which is > 100")
                return True
            return False
        except TypeError:
            print("Error: Unable to check win conditions due to invalid player data.")

    def play(self):
        try:
            while True:
                print("\n" + "=" * 20)
                print(f"It's {self.current_player.name}'s turn.")
                print(f"{self.current_player.name}'s Balance: {self.current_player.balance}")
                print(f"{self.current_player.name}'s Debt: {self.current_player.debt}")
                self.board.display_board([self.player1, self.player2])
                
                input("Press Enter to roll the dice...")
                outcome = self.current_player.roll_dice()
                print(f"{self.current_player.name} rolled: {outcome}")

                if outcome in [1, 2, 3]:
                    self.current_player.move(outcome)
                    self.board.display_board([self.player1, self.player2])
                    self.current_player.apply_board_effect(self.board, self.player2 if self.current_player == self.player1 else self.player1)
                
                print(f"Updated Balance for {self.current_player.name}: {self.current_player.balance}")
                print(f"Updated Debt for {self.current_player.name}: {self.current_player.debt}")

                if self.check_and_print_win_conditions():
                    break

                self.switch_player()
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
