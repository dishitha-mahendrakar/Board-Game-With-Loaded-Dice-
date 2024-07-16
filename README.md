# Board Game With Loaded Dice

## Overview
This is a CLI-based 2-player circular board game where players move based on dice rolls and perform actions based on the square they land on. The goal is to have a balance minus debt greater than 100.

## Requirements
- Python 3.x

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run `python game.py` to start the game.

## Game Rules
- Players start with a balance of 5 and a debt of 0.
- The board has different types of squares (Bank, Jail, House).
- Players roll a loaded dice to determine their moves.
- The game ends when a player's balance minus debt exceeds 100.

## Unit Tests
Run `python -m unittest discover` to execute the unit tests.

## Assumptions
- The game board and the rules are predefined and hardcoded.
- The dice rolls are simulated with random choices.

## Code Structure
- `player.py`: Defines the Player class.
- `board.py`: Defines the Board class and dice logic.
- `game.py`: Defines the Game class and coordinates the game flow.
- `test_game.py`: Contains unit tests for the game.

## Design Principles
- Follows OOP principles for modular and reusable code.
- Includes comments and proper variable naming conventions.
- Provides unit tests to ensure correctness.
