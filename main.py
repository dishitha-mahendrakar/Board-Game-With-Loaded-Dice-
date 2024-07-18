from game import Game

if __name__ == "__main__":
    try:
        player1_name = input("Enter Player 1's name: ")
        player2_name = input("Enter Player 2's name: ")

        game = Game(player1_name, player2_name)
        game.play()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
