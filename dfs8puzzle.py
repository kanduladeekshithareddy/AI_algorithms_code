def moves( mats):
    movearray=[]
    for i in range(0,3):
        for j in range(0,3):
            if (mats[i][j]==0):#for blanc space 
                row,col=i,j
    rc=[[0,1],[1,0],[0,-1],[-1,0]] #to move up down left right
    for ro,co in rc:
        nrow,ncol=row+ro,col+co
        if (0<=nrow<3 and 0<=ncol<3):
            newstate=[]
            for i in range(0,3):
                ans=[]
                for j in range(0,3):
                    ans.append(mats[i][j])
                newstate.append(ans)
            newstate[row][col], newstate[nrow][ncol]=newstate[nrow][ncol],newstate[row][col]
            movearray.append(newstate)
    return movearray

def dfs(init):
    stack=[]
    path=[]
    stack.append((init,path))
    visited=set()
    
    while stack:
         nowstate,path=stack.pop()
         if (goal == nowstate):
             return path
         nowstup= tuple(map(tuple, nowstate))
         visited.add(nowstup)
         nextstate=moves(nowstate)
         for state in nextstate:
             statetup=tuple(map(tuple, state))
             if statetup not in visited :
                stack.append((state, path+[state]))
                visited.add(statetup)
    print(len(path))
    return None


mat=[[1,2,3],[4,5,6],[0,7,8]] #initial state of matrix
print(mat)
# print(moves(mat))
goal=[[1,2,3],[4,5,6],[7,8,0]] #goal state of matrix
print(goal,"\n")
solpath=dfs(mat)
if solpath:
    for step,state in enumerate(solpath):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
else:
   print("no solution")