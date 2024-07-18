class Board:
    def __init__(self):
        self.board_layout = [
            ['H', 'B', 'H', 'J'],
            ['H', ' ', ' ', 'B'],
            ['J', ' ', ' ', 'H'],
            ['H', 'H', 'B', 'B']
        ]
        self.positions = [
            [1, 2, 3, 4],
            [12, ' ', ' ', 5],
            [11, ' ', ' ', 6],
            [10, 9, 8, 7]
        ]

    def display_board(self, players):
        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                for player in players:
                    if player.position == self.positions[i][j]:
                        print(f"{player.name[0]}", end=" ")
                        break
                else:
                    print(self.board_layout[i][j], end=" ")
            print()
