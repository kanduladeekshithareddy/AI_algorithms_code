def gaschnigs_heuristic(board, goal):
    n = len(board)
    h = 0
    # Step i: Move mismatched tiles into the blank
    for i in range(n):
        for j in range(n):
            if board[i][j] != goal[i][j]:
                h += 1
    # Step ii: Find the tile that should go in the blank's location and teleport it there
    blank_row, blank_col = find_blank_position(board, n)
    goal_tile = goal[blank_row][blank_col]

    for i in range(n):
        for j in range(n):
            if board[i][j] == goal_tile:
                h += 1
    return h


def find_blank_position(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:  # 0 represents the blank tile
                return i, j

# Example usage
current_board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  # Current state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]    # Goal state

heuristic_value = gaschnigs_heuristic(current_board, goal_state)
print("Gaschnig's Heuristic Value:", heuristic_value)
