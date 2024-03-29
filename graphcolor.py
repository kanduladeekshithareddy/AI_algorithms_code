import random,math
k=3
visited=set()
adjmatrix=[[0]*k for _ in range(k)]
points=[[1,1],[2,2],[1,2]]
lines=set() #set is tuple of points in which line is connected
#for selecting a random value initially
def selection():
    pind=random.rand(0,3)
    while pind not in visited:
          pind=random.rand(0,3)
    return pind
# to find the distance between the points   
def distance(point1,point2):
    y=point2[1]-point1[1]
    x=point2[0]-point1[0]
    p= x*x + y*y
    return math.sqrt(p)
#asked the nearest neighbour of the randomly selected point   
def nearest(t):
    point1=points[t]
    min=float('inf')
    pointret=[]
    for i in range (len(points)):
        if i!=t:
           p=distance (point1,points[i])
           if(min>p):
             min=p
             pointret=i
    return pointret
#for finding the intersection point of two lines 
def findintersect(point1, point2, point3, point4):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4

    # Calculate the slopes of the two lines
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y4 - y3) / (x4 - x3)

    # Calculate the intersection point
    x_intersection = (slope1 * x1 - y1 - slope2 * x3 + y3) / (slope1 - slope2)
    y_intersection = slope1 * (x_intersection - x1) + y1

    return x_intersection, y_intersection
#to check if two lines are crossing 
def crosscheck(p,q,p1,p2):
    res=()
    p=selection()
    q=nearest(p)
    if lines==None:
        lines.add((p,q))
    else:
        for i,j in lines:
            x,y=findintersect(i,j,points[p],points[q])
            if (x,y) in points:
                res.append((p,q))
    for i in res:
        lines.add(i)
    print(lines)
def isSafe(vertex,color,graph,colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True
def color_graph(graph, num_colors, colors, vertex):
    if vertex == len(graph):
        return True
    
    for color in range(1, num_colors + 1):
        if isSafe(vertex, color, graph, colors):
            colors[vertex] = color
            if color_graph(graph, num_colors, colors, vertex + 1):
                return True
            colors[vertex] = 0  # Backtrack by resetting the color
    
    return False

def graph_coloring(graph, num_colors):
    num_vertices = len(graph)
    colors = [0] * num_vertices
    
    if color_graph(graph, num_colors, colors, 0):
        print("Graph can be colored with", num_colors, "colors.")
        print("Coloring:", colors)
    else:
        print("Graph cannot be colored with", num_colors, "colors.")
if __name__=='__main__':
    adjmatrix=[[0, 1, 1, 1],[1, 0, 1, 0],[1, 1, 0, 1],[1, 0, 1, 0]]
    num_colors=3
    graph_coloring(adjmatrix,num_colors)