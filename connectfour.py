import pprint

class Board:

    def __init__(self):
        self.grid = self.get_grid()
        self.player = 1

    def get_grid(self):
        grid = [[0, 0, 0, 0, 0, 0, 0] for _ in range(7)]
        return grid

    def play(self, pos):
        for i in range(7):
            if self.grid[i][pos] == 0:
                self.grid[i][pos] = self.player
                if self.player == 1:
                    self.player = 2
                else:
                    self.player = 1
                return
        print("invalid entry")

    def print_board(self):
        for i in reversed(range(7)):
            line = ['|']
            for j in range(7):
                if self.grid[i][j] == 0:
                    line.append('.')
                elif self.grid[i][j] == 1:
                    line.append('X')
                elif self.grid[i][j] == 2:
                    line.append('O')
            line.append('|')
            print(line)


game = Board()
game.play(2)
game.play(4)
game.play(2)

# pprint.pprint(game.grid)
game.print_board()







