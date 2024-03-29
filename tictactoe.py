class node:
    def __init__(self, play, mat, util):
        self.p = play
        self.b = mat
        self.u = util

    def successors(self):
        moves = []
        ply = self.p
        for i in range(3):
            for j in range(3):
                if self.b[i][j] == " ":
                    mat = [row[:] for row in self.b]  # Create a copy of the board
                    if ply == 'max':
                        mat[i][j] = 'X'
                        p = node('min', mat, float('inf'))
                    else:
                        mat[i][j] = 'O'
                        p = node('max', mat, float('-inf'))
                    moves.append(p)
        return moves

def terminaltest(mat):
    for row in mat:  # for row check
        if row[0] == row[1] and row[0] == row[2] and row[1] == row[2] and row[0] != ' ':
            return row[0], True
    for col in range(3):  # for col check
        if mat[0][col] == mat[1][col] and mat[0][col] == mat[2][col] and mat[1][col] == mat[2][col] and mat[0][col] != ' ':
            return mat[0][col], True
    if (mat[0][0] == mat[1][1] and mat[0][0] == mat[2][2] and mat[1][1] == mat[2][2]) and mat[0][0] != ' ':
        return mat[0][0], True

    if (mat[0][2] == mat[1][1] and mat[0][2] == mat[2][0] and mat[1][1] == mat[2][0]) and mat[0][2] != ' ':
        return mat[0][2], True
    return None, False

def utility(mat):
    let, _ = terminaltest(mat)
    if let == 'X':
        return 1
    elif let == 'O':
        return -1
    else:
        return 0

def maxvalue(mats):
    p, q = terminaltest(mats.b)
    if q:
        mats.u = utility(mats.b)
        print(mats.b,"max",mats.u)
        return mats.u
    v = float('-inf')
    for child in mats.successors():
        v = max(v, minvalue(child))
    mats.u = v
    return v

def minvalue(mat):
    p, q = terminaltest(mat.b)
    if q:
        print(mat.b,"min")
        mat.u = utility(mat.b)
        return mat.u
    v = float('inf')
    for child in mat.successors():
        v = min(v, maxvalue(child))
    mat.u = v
    return v

def minimax(mat):
    mats = node('max', mat, float('-inf'))
    v = maxvalue(mats)
    best_move = None
    for child in mats.successors():
        if child.u == v:
            best_move = child
    return best_move

# Example usage:
initial_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
best_move = minimax(initial_board)
print("Best Move:")
if best_move :
    for row in best_move.b:
        print(row)
else:
    print("It is showing none")
