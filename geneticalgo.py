import random,time
class Qnode:
    def __init__(self,mat):
        self.pos=mat
    def fitness(self):
        count=0
        for i in range(0,8):
            for j in range(i+1,8):
                if self.pos[i]!=self.pos[j] and abs(j-i)!=abs(self.pos[j]-self.pos[i]):
                   count+=1
        return count
def selection(pops):
    fitnesslist=[]
    for j in range(len(pops)):
        l=pops[j]
        f=l.fitness()
        fitnesslist.append(f)
    x=random.choices(pops, weights=fitnesslist,k=1)
    y=random.choices(pops, weights=fitnesslist,k=1)
    return x[0],y[0]
        
def crossover(qpos1,qpos2):
    i=random.randrange(8)
    temp1=qpos1[:i]+qpos2[i:]
    temp2=qpos2[:i]+qpos1[i:]
    p,q=Qnode(temp1),Qnode(temp2)
    return p,q
def mutation(node):
    mat = node.pos
    i = random.randrange(8)
    j = random.randrange(8)
    while i == j:
        j = random.randrange(8)
    mat[i], mat[j] = mat[j], mat[i]
def geneticalgo(population,exectime):
    for child in population:
        if child.fitness() == 0:
            return child
    
    while time.time()-starttime<exectime:
        newpop = []
        for _ in range(int(len(population)/2)):
            x, y = selection(population)
            child1, child2 = crossover(x.pos, y.pos)
            newpop.append(child1)
            newpop.append(child2)
        population = newpop
        for child in population:
            if child.fitness() == 0:
                return child
    return None

if __name__ == "__main__":
    population=[]
    for i in range(0,4):
        ans=[]
        for j in range(0,8):
            x=random.randrange(0,8)
            ans.append(x)
        p=Qnode(ans)
        population.append(p)
    starttime=time.time()
    res=geneticalgo(population,20)
    endtime=time.time()
    if res==None:
        print("no solution")
    else:
        print(res.pos)
    print("timetaken:",(endtime-starttime))
