import heapq
import time
import psutil
class Node:
    def __init__(self, state, parent, depth):
        self.node = state
        self.parent = parent
        self.d = depth

    def __lt__(self, other):
        return (self.d + self.manhatd(goal)) < (other.d + other.manhatd(goal)) #calculation of f value= depth + cost*w

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
        t=abs(self.manhatd(goal)-state.manhatd(goal))
        if (t<=1):
            return True
        else:
            return False

    def manhatd(self, goal):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.node[i][j] != 0:  # Skip the blank tile
                    goal_row, goal_col = find_position(goal, self.node[i][j])
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance

def find_position(grid, num):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == num:
                return i, j

def idastar(start, goal,flimit,count):
    state = Node(initial, None, 0)
    heap = [state]
    visited = set()
    while heap:
        nowstate = heapq.heappop(heap)
        min=nowstate.manhatd(goal)+nowstate.d
        if (flimit<min):
            flimit=min
            print(flimit,nowstate.node)
            return None,count,flimit
        visited.add(tuple(tuple(row) for row in nowstate.node))
        if nowstate.node == goal:
            return nowstate,count,flimit
        for child in nowstate.moves():
            count+=1
            nowtup = tuple(tuple(row) for row in child.node)
            if nowtup not in visited:
                cf=child.manhatd(goal)+child.d
                heapq.heappush(heap,child)
    return None,count,flimit
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
    nstate = Node(initial, None, 0)
    f=nstate.manhatd(goal)+nstate.d
    solpath=None
    while f and not solpath:
        solpath ,count,f= idastar(initial, goal,f,0)
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