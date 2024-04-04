import random

class Minesweeper:
    def __init__(self, size=3):
        self.board = [['?' for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_bomb(self, bomb_location):
        # Place a bomb at a random location on the board
        bomb_row, bomb_col = bomb_location
        self.board[bomb_row][bomb_col] = 'X'

    def show_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def cek_bomb(self, row, col):
        bomb = 0
        for r in range(max(0, row-1), min(self.size, row+2)):
            for c in range(max(0, col-1), min(self.size, col+2)):
                if self.board[r][c] == 'X':
                    bomb += 1
        return bomb

    def open_box(self, bomb_location, row, col):
        if self.board[row][col] != '?':
            print("This box is already open.")
            return False

        if (row, col) == bomb_location:
            return True  # Hit the bomb

        bomb_count = self.cek_bomb(row, col)
        self.board[row][col] = 'O' if bomb_count == 0 else str(bomb_count)
        return False

    def check_win(self, bomb_location):
        # Check if all cells except the bomb and opened cells are marked
        for r in range(self.size):
            for c in range(self.size):
                if (r, c) != bomb_location and self.board[r][c] == '?':
                    return False
        return True

    def play_game(self):
        self.bomb_location = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.add_bomb(self.bomb_location)

        while True:
            self.show_board()
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if row < 0 or row >= self.size or col < 0 or col >= self.size:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Please enter numbers only.")
                continue

            if self.open_box(self.bomb_location, row, col):
                print("Yikes! You found a bomb. The End")
                self.board[self.bomb_location[0]][self.bomb_location[1]] = 'X'
                self.print_board(self.board)
                break
            elif self.check_win(self.bomb_location):
                print("Congratulations! You win the game!")
                self.print_board(self.board)
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play_game()