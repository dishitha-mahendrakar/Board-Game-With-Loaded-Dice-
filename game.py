# Import necessary modules
from player import Player
from board import Board
import random

# Define the Game class
class Game:
    # Constructor to initialize the game with two players and a game board
    def __init__(self, player1_name, player2_name):
        # Create a new instance of the game board
        self.board = Board()
        # Create player objects for player 1 and player 2
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        # Set the current player to player 1 at the start of the game
        self.current_player = self.player1

    # Method to switch the turn to the next player
    def switch_player(self):
        # Check which player's turn it currently is and switch to the other player
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    # Method to check win conditions and print the winner if conditions are met
    def check_and_print_win_conditions(self):
        # Determine who the opponent player is
        self.opponent_player = self.player1 if self.current_player == self.player2 else self.player2

        # Calculate balance and debt differences for the current player and the opponent
        current_player_balance_check = self.current_player.balance - self.current_player.debt
        current_player_debt_check = self.current_player.debt - self.current_player.balance
        opponent_player_balance_check = self.opponent_player.balance - self.opponent_player.debt
        opponent_player_debt_check = self.opponent_player.debt - self.opponent_player.balance
        
        # Check win conditions and print the winner
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
        # Return False if no win conditions are met
        return False

    # Method to start and run the game
    def play(self):
        # Start a continuous loop until a player wins
        while True:
            # Display the current player's turn and their financial status
            print("\n" + "=" * 20)
            print(f"It's {self.current_player.name}'s turn.")
            print(f"{self.current_player.name}'s Balance: {self.current_player.balance}")
            print(f"{self.current_player.name}'s Debt: {self.current_player.debt}")
            print("current board state : ")
            # Display the current state of the game board
            self.board.display_board([self.player1, self.player2])
            
            # Wait for user input to roll the dice
            input("Press Enter to roll the dice...")
            # Roll the dice for the current player and display the outcome
            outcome = self.current_player.roll_dice()
            print(f"{self.current_player.name} rolled: {outcome}")

            # Process the outcome of the dice roll
            if outcome in [1, 2, 3]:
                # Move the current player on the board
                self.current_player.move(outcome)
                # Display the updated board state after the move
                self.board.display_board([self.player1, self.player2])
                # Apply board effects based on the player's new position
                self.current_player.apply_board_effect(self.board, self.player2 if self.current_player == self.player1 else self.player1)
            
            # Display the updated balance and debt for the current player
            print(f"Updated Balance for {self.current_player.name}: {self.current_player.balance}")
            print(f"Updated Debt for {self.current_player.name}: {self.current_player.debt}")

            # Check win conditions after each move
            if self.check_and_print_win_conditions():
                break  # Exit the loop if a player has won

            # Switch to the next player's turn
            self.switch_player()
