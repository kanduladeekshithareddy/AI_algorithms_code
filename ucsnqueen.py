import heapq

class Node:
    def __init__(self):
        self.arr = [[0 for _ in range(4)] for _ in range(4)]
        self.row = -1
        self.column = 0

    def __lt__(self, other):
        return self.row < other.row

def print_board(arr):
    for row in arr:
        print(" ".join(map(str, row)))
    print()

def is_valid(a):
    for i in range(a.row):
        if a.arr[i][a.column] == 1:
            return False
        if a.column - (a.row - i) >= 0 and a.arr[i][a.column - (a.row - i)] == 1:
            return False
        if a.column + (a.row - i) < 4 and a.arr[i][a.column + (a.row - i)] == 1:
            return False
    return True

def solve_n_queens():
    start = Node()
    heap = [start]

    while heap:
        current = heapq.heappop(heap)
        if current.row == 3:
            print_board(current.arr)
            return

        for i in range(4):
            child = Node()
            for j in range(4):
                child.arr[j] = current.arr[j].copy()
            child.row = current.row + 1
            child.column = i
            child.arr[child.row][i] = 1

            if is_valid(child):
                heapq.heappush(heap, child)

if __name__ == "__main__":
    solve_n_queens()
