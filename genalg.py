import random,time

class Qnode:
    def __init__(self, mat):
        self.pos = mat

    def fitness(self):
        count = 0
        for i in range(0, 8):
            for j in range(i + 1, 8):
                if self.pos[i] != self.pos[j] and abs(j - i) != abs(self.pos[j] - self.pos[i]):
                    count += 1
        return count

def random_selection(pops):
    fitnesslist=[]
    for j in range(len(pops)):
        l=pops[j]
        f=l.fitness()
        fitnesslist.append(f)
    return random.choices(pops, weights=fitnesslist,k=1)[0]

def reproduce(x, y):
    i = random.randrange(8)
    child1 = x[:i] + y[i:]
    child2 = y[:i] + x[i:]
    return child1, child2

def mutate(child):
    i = random.randrange(8)
    j = random.randrange(8)
    
    # Ensure i and j are distinct positions
    while i == j:
        j = random.randrange(8)
    
    # Swap positions i and j
    child[i], child[j] = child[j], child[i]

def genetic_algorithm(population,exectime):
    while time.time()-starttime<exectime:
        new_population = []
        
        # Check if any individual in the population is fit enough
        for individual in population:
            if individual.fitness() == 0:
                return individual
        
        for _ in range(len(population)):
            x = random_selection(population)
            y = random_selection(population)
            child1, child2 = reproduce(x.pos, y.pos)
            
            # Apply mutation with a small random probability
            if random.random() < 0.1:  # Adjust the mutation probability as needed
                mutate(child1)
            if random.random() < 0.1:
                mutate(child2)
            
            # Create Qnode objects for the children
            child1_node = Qnode(child1)
            child2_node = Qnode(child2)
            
            # Add children to the new population
            new_population.append(child1_node)
            new_population.append(child2_node)
        
        # Update the population with the new generation
        population = new_population

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
    res=genetic_algorithm(population,10)
    endtime=time.time()
    if res==None:
        print("no solution")
    else:
        print(res.pos)
    print("timetaken:",(endtime-starttime))
