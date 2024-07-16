class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_player = player1

    def play_turn(self):
        if self.current_player.miss_next_turn:
            print(f"{self.current_player.name} misses this turn.")
            self.current_player.miss_next_turn = False
        else:
            steps = self.board.roll_dice()
            print(f"{self.current_player.name} rolls a {steps}")
            self.current_player.move(steps, self.board)
        self.switch_player()

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def display_board(self):
        board_str = ''.join(self.board.squares)
        p1_pos = self.current_player.position
        p2_pos = self.player2.position if self.current_player == self.player1 else self.player1.position
        board_str = board_str[:p1_pos] + '1' + board_str[p1_pos+1:]
        board_str = board_str[:p2_pos] + '2' + board_str[p2_pos+1:]
        print(f"Board: {board_str}")

    def check_winner(self):
        p1_net = self.player1.balance - self.player1.debt
        p2_net = self.player2.balance - self.player2.debt
        if p1_net > 100:
            print(f"{self.player1.name} wins!")
            return True
        if p2_net > 100:
            print(f"{self.player2.name} wins!")
            return True
        return False

    def play_game(self):
        while not self.check_winner():
            self.display_board()
            self.current_player.display_status()
            self.play_turn()
            self.current_player.display_status()

# Example of how to run the game
if __name__ == "__main__":
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    board = Board("HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH")
    game = Game(p1, p2, board)
    game.play_game()
