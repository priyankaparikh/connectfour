import pprint
import random

class Board:

    def __init__(self):
        self.grid = self.get_grid()
        self.player = 1


    def get_grid(self):
        """Generate a new grid for the game board.
        """

        grid = [[0, 0, 0, 0, 0, 0, 0] for _ in range(7)]
        return grid


    def play(self, pos):
        """Given a position from 0-7 update the grid in the first available spot.
        """

        for i in range(7):
            if self.grid[i][pos] == 0:
                self.grid[i][pos] = self.player
                if self.winner(pos, i):
                    print("Congratulations player {} wins".format(self.player))
                if self.player == 1:
                    self.player = 2
                else:
                    self.player = 1
                return
        print("invalid entry")


    def print_board(self):
        """Print a readable representation of the grid for players.
        """

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
            print(' '.join(line))


    def legal_moves(self):
        """
        Check the grid to Return a list of available moves.
        """

        legal_moves = []

        for i in range(7):
            if self.grid[i][-1] == 0:
                legal_moves.append(i)

        return legal_moves


    def make_move(self):
        """AI uses random to choose a number from the list of available legal moves
        """
        available_moves = self.legal_moves()
        chosen_move = random.randrange(len(available_moves + 1))
        pos = available_moves[chosen_move]


    def winner(self, pos, i):
        """Return if the current move at position (pos) in
        row (i) is a winning move. This is done at each move both
        the players make.

        keyword args:
        pos : int (posiiton of the move)
        i : int (row number in the grid)
        """
        def check_vertical(pos):
            """Check if the move is a winning move veritcally. 
            """

            count = 0
            for i in range(7):
                if count == 4:
                    return True
                elif self.grid[i][pos] == self.player:
                    count += 1
                else:
                    count = 0
            return count == 4

        def check_horizontal(pos, i):
            """Check if the current player is a winner along the row.
            """

            count = 0
            for move in self.grid[i]:
                if count == 4:
                    return True
                elif move == self.player:
                    count += 1
                else:
                    count = 0
            return count == 4

        def check_diagonal(pos, i):
            """Check if the current played move is a winning move along the diagonals.
            """
            pass

        return check_vertical(pos) or check_horizontal(pos, i) or check_diagonal(pos, i)


game = Board()
game.play(1)
pprint.pprint(len(game.legal_moves()))
game.play(1)
game.play(2)
game.play(2)
game.play(3)
game.play(3)
pprint.pprint(len(game.legal_moves()))
game.play(4)

# pprint.pprint(game.grid)
game.print_board()







