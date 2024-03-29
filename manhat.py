start = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
def manhattan_distance(puzzle, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:  # Skip the blank tile
                goal_row, goal_col = find_position(goal, puzzle[i][j])
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def find_position(grid, num):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == num:
                return i, j

# Example puzzle and goal states (0 represents the blank tile)
distance = manhattan_distance(start, goal)
print("Manhattan Distance:", distance)
