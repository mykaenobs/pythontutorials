class TicTacToe:
    def __init__(self, board)
        self.board = ['' for _ in range(9)] # this is for the board


    def print_board(self)
        for row in [self.board(i*3:(i+1)*3) for i in range(3)]
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def avaliable_moves(self):
        # list comprehension
        return [i for i, spot in enumerate(self.board) if spot == ' ']


def play(game, x_player, e_player, print_game=True):
    if print_game:
        game.print_board_nums

    letter = 'x'