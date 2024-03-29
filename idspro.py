class Node:
    def __init__(self, state, x, y, parent):
        self.state = state
        self.blank_x = x
        self.blank_y = y
        self.parent = parent
    
    def successor(self):
        children = []
        # up, down, left, right
        actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        p = Node(self.state, self.blank_x, self.blank_y, self.parent)
        
        for action in actions:
            new_blank_x = self.blank_x + action[0]
            new_blank_y = self.blank_y + action[1]
            child = [row[:] for row in self.state]
            
            if 0 <= new_blank_x < 3 and 0 <= new_blank_y < 3:
                child[self.blank_x][self.blank_y] = child[new_blank_x][new_blank_y]
                child[new_blank_x][new_blank_y] = 0
                children.append(Node(child, new_blank_x, new_blank_y, p))
        
        return children
    
    def is_goal(self, goal):
        return self.state == goal
    
    def print_state(self):
        for row in self.state:
            print(' '.join(map(str, row)))
        print('')

def dfs(start, goal,limit):
    stack = []
    visited = set()
    stack.append((start,0))
    visited.add(tuple(map(tuple, start.state)))
    flag = False

    while stack:
        curr,nodelim = stack.pop()
        flag = curr.is_goal(goal)
        if (nodelim==limit):
            continue
        if flag:
            return path(curr)
        
        children = curr.successor()
        for child in children:
            if tuple(map(tuple, child.state)) not in visited:
                stack.append((child,nodelim+1))
                visited.add(tuple(map(tuple, child.state)))

    return None

def path(last):
    path_list = []
    while last:
        path_list.append(last.state)
        last = last.parent
    return path_list

if __name__ == "__main__":
    start_state = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    limit=50
    count=0
    s = Node(start_state, 1, 0, None)
    for i in range(limit):
        solution_path = dfs(s, goal_state,limit)
        if solution_path:
            print("Path size is --->", len(solution_path))
            for state in solution_path:
                for row in state:
                    print(' '.join(map(str, row)))
                print('')
            break
        else:
            print("No solution found.")
