# Board Game With Loaded Dice

## Overview
This is a CLI-based 2-player circular board game where players move based on dice rolls and perform actions based on the square they land on. The goal is to have a balance minus debt greater than 100.

## Requirements
- Python 3.x

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run `python3 main.py` to start the game.

## Game Rules
- Players start with a balance of 5 and a debt of 0.
- The board has different types of squares (Bank, Jail, House).
- Players roll a loaded dice to determine their moves.
- The game ends when a player's balance minus debt exceeds 100 or when the opponent's debt minus balance exceeds 100.

## Unit Tests
Run `python3 test_board.py ` to execute the unit tests.
Run `python3  test_game.py ` to execute the unit tests.
Run `python3 test_player.py` to execute the unit tests.
Run `python3 test_main.py` to execute the unit tests.

## Assumptions
- The game board and the rules are predefined and hardcoded.
- The dice rolls are simulated with random choices and are based on the probability mentioned.
  

## Code Structure
- `player.py`: Defines the `Player` class which manages player attributes (`name`, `balance`, `debt`, `position`) and methods for player actions (`update_balance`, `roll_dice`, `move`, `take_loan`, `repay_loan`, `apply_board_effect`).

- `board.py`: Defines the `Board` class which handles the game board's layout (`board_layout`) and positions (`positions`). Includes a method (`display_board`) to visualize the board state.

- `game.py`: Defines the `Game` class which coordinates the game flow. It initializes instances of `Player` and `Board`, manages player turns (`switch_player`), checks win conditions (`check_and_print_win_conditions`), and drives the game execution (`play` method).

- `main.py`: Entry point for starting the game. Prompts users to input player names, creates a `Game` instance, and initiates the game loop (`game.play()`).

- `test_player.py`: Unit tests for the `Player` class. Tests cover initialization, balance updates, dice rolling, and board effects handling.

- `test_game.py`: Unit tests for the `Game` class. Tests include initialization, player switching, win condition checking, and game execution flow.

- `test_board.py`: Unit tests for the `Board` class. Tests cover board initialization, position tracking, and board state display.

- `test_main.py`: Unit tests for the main game execution flow (`main.py`). Tests simulate user inputs and check game outcomes, including handling interruptions.

## Design Principles

In the provided code across `player.py`, `game.py`, `board.py`, and `main.py`, several Object-Oriented Programming (OOP) principles are observed. Here's how each file adheres to these principles:

### 1. Encapsulation
- player.py:
The Player class encapsulates attributes like name, balance, debt, and position within its instance.
Methods like update_balance, roll_dice, move, take_loan, repay_loan, and apply_board_effect encapsulate related functionalities, ensuring that the internal state of a Player object is manipulated through well-defined interfaces.
- game.py:
The Game class encapsulates the game state, including board, player1, player2, and current_player.
Methods like switch_player, check_and_print_win_conditions, and play encapsulate game logic, controlling the flow and interactions between players and the game board.
- board.py:
The Board class encapsulates the game board's layout (board_layout and positions) and provides methods (display_board) to interact with and display the board state.
- main.py:
Encapsulates the game initiation and execution within game.py's Game class.

### 2. Abstraction
- player.py:
Abstracts player-related functionalities such as balance management (update_balance), dice rolling (roll_dice), movement (move), loan handling (take_loan, repay_loan), and board effects (apply_board_effect).
- game.py:
Abstracts game-related logic such as player turns (switch_player), win condition checking (check_and_print_win_conditions), and game execution (play).
- board.py:
Abstracts board-related data (board_layout and positions) and operations (display_board).

### 3. Polymorphism
- player.py:
The roll_dice method exhibits polymorphic behavior by handling different outcomes (1, 2, 3, "RollAgain") with varying probabilities.
- board.py:
The display_board method demonstrates polymorphism by displaying different representations ('H', 'B', 'J', empty spaces) based on the current game state.

### 4. Encapsulation (continued)
- player.py:
Encapsulates player-specific data (name, balance, debt, position) and operations (update_balance, roll_dice, move, take_loan, repay_loan, apply_board_effect) within the Player class.
Data is accessed and modified through controlled methods, ensuring proper validation and encapsulation.
- game.py:
Encapsulates game-specific data (board, player1, player2, current_player) and operations (switch_player, check_and_print_win_conditions, play) within the Game class.
Interactions between players and the board are encapsulated, maintaining clear boundaries of responsibility.

- board.py:
Encapsulates board-related data (board_layout and positions) and operations (display_board) within the Board class.
Provides methods to interact with the board state while hiding its internal representation.

### 5. Polymorphism
- player.py:
The roll_dice method demonstrates polymorphic behavior by handling different outcomes (1, 2, 3, "RollAgain") with varying probabilities.
- board.py:
The display_board method demonstrates polymorphism by displaying different representations ('H', 'B', 'J', empty spaces) based on the current game state.
### 6. Composition
- game.py:
The Game class uses composition to include instances of Player and Board classes (self.player1, self.player2, self.board).
- main.py:
Uses composition to initiate and manage the Game instance (game = Game(player1_name, player2_name)).

### 7. Dependency Injection
- player.py, game.py, board.py:
Instances of dependent classes (Player in Game, Board in Game) are injected into constructors (__init__ methods) rather than being instantiated within the class. This allows for better testing and flexibility in changing dependencies.

## Summary
The provided code adheres to several key principles of Object-Oriented Programming (OOP), such as encapsulation, abstraction, polymorphism, and composition. These principles help in structuring the codebase in a modular and maintainable manner, with clear responsibilities assigned to each class and method.
