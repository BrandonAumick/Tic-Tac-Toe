from random import randint

class Board():
    def __init__(self):
        self.board = []
        self.size = randint(3, 10)
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        for i in range(self.size ** 2):
            self.board.append(f"{i:02d}".translate(SUB)) # Creates an array for the board
        turn = 0
        symbols = ('X', 'O')

    def printBoard(self):
        print(self.size)
        for i in range(self.size ** 2):
            if i != 0:
                print('\n' + int(4.8 * self.size) * '-') if (i % self.size) == 0 else print(' | ', end ="")
            print(f'{self.board[i]}', end = "")

if __name__ == '__main__':
    game = Board()
    game.printBoard()
