from random import randint

class Board():
    def __init__(self, inputSize):
        self.size = inputSize
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.board = [f'{x:02d}'.translate(SUB) for x in range(self.size ** 2)]
        self.turn = 1
        self.symbols = ('  X  ', '  O  ')  # Symbols have a hair+thin space before/after them to match number spacing

    def print_board(self):
        for i in range(self.size ** 2):
            if i != 0:
                print('\n' + int(4.8 * self.size) * '-') if (i % self.size) == 0 else print(' | ', end ="")
            print(self.board[i], end = "")

    def make_move(self):
        try:
            playerChoice = int(input(f'\nPlayer {self.turn + 1}:'))
        except:
            playerChoice = -1  # Defaults to invalid choice for a character input
        if playerChoice in range(len(self.board)) and not self.symbols.__contains__(self.board[playerChoice]):
            self.board[playerChoice] = self.symbols[self.turn]
        else:
            print("Invalid Input")
            self.make_move()

    def check_win(self):
        # Check horizontally
        for row in range(self.size):
            for column in range(self.size - 1):
                if not self.board[column + (row * self.size)] == self.board[column+1 + (row * self.size)]:
                    break
            else:
                return True
        # Check vertically
        for column in range(self.size):
            for row in range(self.size - 1):
                if not self.board[(row * self.size) + column] == self.board[((row+1) * self.size) + column]:
                    break
            else:
                return True
        # Check diagonally right
        for i in range(self.size - 1):
            if not self.board[i * (self.size + 1)] == self.board[(i + 1) * (self.size + 1)]:
                break
        else:
            return True
        # Check diagonally left
        for i in range(1, self.size):
            if not self.board[(self.size - 1) * i] == self.board[(self.size - 1) * (i + 1)]:
                break
        else:
            return True

    def game_loop(self):
        turnCount = 0  # Counts the number of turns played
        while not self.check_win():
            if turnCount == len(self.board):  # When all possible turns have been played it prints "draw"
                print("Draw")
                return
            self.turn = (self.turn + 1) % 2
            self.print_board()
            self.make_move()
            turnCount += 1
        print(f'\nPlayer {self.turn + 1} wins')  # Prints a winner if the loop ends without a draw return

if __name__ == '__main__':
    game = Board(randint(3, 10))
    game.game_loop()
