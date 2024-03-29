import heapq
import copy
import psutil
import time
class Node:

    def __init__(self, state, parent, gval, hval, flimit):
        self.node = state
        self.parent = parent
        self.g = gval
        self.h = hval
        self.f = self.g + self.h
        self.fl = flimit
        
    def __lt__(self, other):
        return self.f < other.f
    
    def moves(self):
        movearray = []
        for i in range(3):
            for j in range(3):
                if self.node[i][j] == 0:
                    row, col = i, j
        rc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for ro, co in rc:
            nrow, ncol = row + ro, col + co
            if 0 <= nrow < 3 and 0 <= ncol < 3:
                newstate = [row[:] for row in self.node]
                newstate[row][col], newstate[nrow][ncol] = newstate[nrow][ncol], newstate[row][col]
                newnode = Node(newstate, self, self.g + 1, gaschnigs_heuristic(newstate, goal), self.fl)
                movearray.append(newnode)
        return movearray
    
def gaschnigs_heuristic(arr, goal):
    h = 0
    # Step i: Move mismatched tiles into the blank
    for i in range(3):
        for j in range(3):
            if arr[i][j] != goal[i][j]:
                h += 1
    # Step ii: Find the tile that should go in the blank's location and teleport it there
    blank_row, blank_col = find_position(arr)
    goal_tile = goal[blank_row][blank_col]

    for i in range(3):
        for j in range(3):
            if arr[i][j] == goal_tile:
                h += 1
    return h

def find_position(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j

def recursivebestfirstsearch(initial, goal,count):
    intnode = Node(initial, None, 0, gaschnigs_heuristic(initial, goal), float('inf'))
    out, _,c = rbfs(intnode, goal, float('inf'),count)
    return out,c

def rbfs(problem, goal, flimit,count):
    heap = [problem]
    if problem.node == goal:
        return problem, problem.f,count
    while heap:
        nowstate = heapq.heappop(heap)
        for child in nowstate.moves():
            count+=1
            child.f = max(child.f, nowstate.f)
            heapq.heappush(heap, child)
        best = heapq.heappop(heap)  
        if best.f > flimit:
            return None, best.f,count
        if len(heap) > 1:
            alt = heap[0]  
            res, best.f ,count= rbfs(best, goal, min(flimit, alt.f),count)
            if res:
                return res, best.f,count
    return None, float('inf'),count

def path(matrix):
    ans = []
    while matrix.parent is not None:
        ans.append(matrix.node)
        matrix = matrix.parent
    ans.append(matrix.node)  
    ans.reverse()
    return ans

if __name__ == "__main__":
    co=0
    initial = [[5, 3, 0], [8, 7, 6], [2, 4, 1]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    starttime=time.time()
    solpath,count = recursivebestfirstsearch(initial, goal,co)
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