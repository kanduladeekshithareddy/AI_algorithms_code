import heapq
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
def cost(mat ,goal):
    count=0
    for i in range(0,3):
        for j in range (0,3):
            if (mat[i][j]!=goal[i][j]):
                count+=1
    return count

def ucs8puzz(initial,goal):
    heap=[]
    heapq.heappush(heap,(cost(initial,goal),initial,[]))
    visited=set()
    while heap:
        minco,arr,path= heapq.heappop(heap)
        visited.add(tuple(map(tuple, arr)))
        if minco==0:
            return path
        for child in moves(arr):
            statetup=tuple(map(tuple,child))
            if statetup not in visited:
                heapq.heappush(heap,(cost(child,goal),child,path+[child]))
    return None
mat=[[1,2,3],[4,5,6],[0,7,8]] #initial state of matrix
print(mat)
goal=[[1,2,3],[4,5,6],[7,8,0]] #goal state of matrix
print(goal,"\n")
solpath=ucs8puzz(mat,goal)
if solpath:
    for state in enumerate(solpath):
        for row in state:
            print(row)
        print()
else:
   print("no solution")

    

    

