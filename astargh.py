import heapq
import psutil
import time
class Node:
    def __init__(self, state, parent, depth):
        self.node = state
        self.parent = parent
        self.d = depth

    def __lt__(self, other):
        return (self.d + self.gaschnigs_heuristic(goal)) < (other.d + other.gaschnigs_heuristic(goal)) #calculation of f value= depth + cost*w

    def moves(self):
        movearray = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.node[i][j] == 0:
                    row, col = i, j
        rc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for ro, co in rc:
            nrow, ncol = row + ro, col + co
            if 0 <= nrow < 3 and 0 <= ncol < 3:
                newstate = [row[:] for row in self.node]
                newstate[row][col], newstate[nrow][ncol] = newstate[nrow][ncol], newstate[row][col]
                newnode = Node(newstate, self, self.d + 1)
                movearray.append(newnode)
        return movearray
    def consistency(self,state):
        t=abs(self.gaschnigs_heuristic(goal)-state.gaschnigs_heuristic(goal))
        if (t<=1):
            return True
        else:
            return False

    def gaschnigs_heuristic(self, goal):
        h = 0
        # Step i: Move mismatched tiles into the blank
        for i in range(3):
            for j in range(3):
                if self.node[i][j] != goal[i][j]:
                    h += 1
        # Step ii: Find the tile that should go in the blank's location and teleport it there
        blank_row, blank_col = find_position(self.node)
        goal_tile = goal[blank_row][blank_col]

        for i in range(3):
            for j in range(3):
                if self.node[i][j] == goal_tile:
                    h += 1
        return h

def find_position(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j


def astar(initial, goal,count):
    state = Node(initial, None, 0)
    heap = [state]
    visited = set()
    while heap:
        nowstate = heapq.heappop(heap)
        visited.add(tuple(tuple(row) for row in nowstate.node))
        if nowstate.node == goal:
            return nowstate,count
        for child in nowstate.moves():
            count+=1
            # if not child.consistency(child.parent):
            #        print("hello i am not consistent")
            #        return None,count
            nowtup = tuple(tuple(row) for row in child.node)
            if nowtup not in visited:
                heapq.heappush(heap, child)
    return None,count


def path(matrix):
    ans = []
    while matrix.parent is not None:
        ans.append(matrix.node)
        matrix = matrix.parent
    ans.reverse()
    return ans

if __name__ == "__main__":
    initial = [[5, 3, 0], [8, 7, 6], [2, 4, 1]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    starttime=time.time()
    solpath ,count= astar(initial, goal,0)
    endtime=time.time()
    if solpath is not None:
        solution_states = path(solpath)
        for state in solution_states:
            for row in state:
                print(row)
            print()
        print("Nodes generated:", count)
    else:
        print("No solution")

    memory_info = psutil.Process().memory_info()
    memory_used = memory_info.rss 
    print("Memory used:", memory_used, "bytes")
    print("Time taken:", (endtime - starttime))