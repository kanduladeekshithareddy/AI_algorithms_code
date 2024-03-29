import heapq
import time

class Node:
    def __init__(self, state, parent, depth):
        self.node = state
        self.parent = parent
        self.d = depth

    def __lt__(self, other):
        return (self.d + self.heuristic(goal)) < (other.d + other.heuristic(goal))

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

    def heuristic(self, goal):
        cost = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.node[i][j] != goal[i][j]:
                    cost += 1
        return cost

def idastar(start, goal, flimit, count):
    state = Node(initial, None, 0)
    heap = [state]
    visited = set()
    
    while heap:
        nowstate = heapq.heappop(heap)
        f = nowstate.heuristic(goal) + nowstate.d

        if f > flimit:
            flimit = f
            continue

        visited.add(tuple(tuple(row) for row in nowstate.node))

        if nowstate.node == goal:
            return nowstate, count

        for child in nowstate.moves():
            count += 1

            # if not child.consistency(nowstate):
            #     print("hello i am not consistent")
            #     return None, count

            nowtup = tuple(tuple(row) for row in child.node)
            if nowtup not in visited:
                heapq.heappush(heap, child)

    return None, count

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
    starttime = time.time()
    nstate = Node(initial, None, 0)
    solpath, count = idastar(initial, goal, nstate.heuristic(goal)+nstate.d, 0)
    endtime = time.time()
    
    print("NUMBER OF NODES GENERATED:", count)
    
    if solpath is not None:
        res = path(solpath)
        for i in res:
            print(i)
            print("\n")
    else:
        print("No Solution")
    
    print("Time taken:", (endtime - starttime))
