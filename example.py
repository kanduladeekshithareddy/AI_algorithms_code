class Node:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.children = []
        self.score = None

    def is_terminal(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return ' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]

    def generate_children(self):
        if not self.is_terminal():
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        new_board = [row[:] for row in self.board]
                        new_board[i][j] = self.player
                        self.children.append(Node(new_board, 'X' if self.player == 'O' else 'O'))

    def minimax(self, maximizing_player):
        if self.is_terminal():
            if self.player == 'X':
                return -1
            elif self.player == 'O':
                return 1
            else:
                return 0

        if maximizing_player:
            max_score = float('-inf')
            for child in self.children:
                score = child.minimax(False)
                max_score = max(max_score, score)
            self.score = max_score
            return max_score
        else:
            min_score = float('inf')
            for child in self.children:
                score = child.minimax(True)
                min_score = min(min_score, score)
            self.score = min_score
            return min_score

    def get_best_move(self):
        best_move = None
        best_score = float('-inf')
        for child in self.children:
            if child.score > best_score:
                best_score = child.score
                best_move = child
        return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def main():
    initial_board = [[' ' for _ in range(3)] for _ in range(3)]
    root = Node(initial_board, 'X')

    print("Initial Board:")
    print_board(initial_board)

    while True:
        root.generate_children()
        root.minimax(True)
        best_move = root.get_best_move()
        print("\nComputer's Move:")
        print_board(best_move.board)
        if best_move.is_terminal():
            if best_move.score == 1:
                print("Computer wins!")
            elif best_move.score == -1:
                print("Player wins!")
            else:
                print("It's a tie!")
            break
        row, col = map(int, input("Enter your move (row col): ").split())
        if initial_board[row][col] == ' ':
            initial_board[row][col] = 'O'
            root = Node(initial_board, 'X')
            print("\nYour Move:")
            print_board(initial_board)
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
