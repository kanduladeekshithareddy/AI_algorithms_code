import random as rnd

class Bayesian:
    def __init__(self, name, parent, cpt):
        self.n = name
        self.p = parent
        self.cpt = cpt

def genrando():
    num = rnd.random()
    return num

def priorsample(topology):
    sample = {}
    while topology:
        t = topology[0]
        topology.pop(0)
        rnum = genrando()
        #print(rnum)
        if t.p==[]:
            if rnum < t.cpt['probabilities'][0]:
                sample[t.n] = t.cpt['values'][0]
            else:
                sample[t.n] = t.cpt['values'][1]
        else:
            parent_values = [sample[parent] for parent in t.p]
            cpt = t.cpt[tuple(parent_values)]
            if rnum < cpt['probabilities'][0]:
                sample[t.n] = cpt['values'][0]
            else:
                sample[t.n] = cpt['values'][1]
    return sample

def genbaynetwork():
    node1 = Bayesian('A', [], {'values': ['a', '-a'], 'probabilities': [0.3, 0.7]})
    node2 = Bayesian('B', ['A'], {('a',): {'values': ['b', '-b'], 'probabilities': [0.1, 0.9]}, ('-a',): {'values': ['b', '-b'], 'probabilities': [0.6, 0.4]}})
    node3 = Bayesian('C', ['A', 'B'], {('a', 'b'): {'values': ['c', '-c'], 'probabilities': [0.05, 0.95]}, ('a', '-b'): {'values': ['c', '-c'], 'probabilities': [0.5, 0.5]}, ('-a', 'b'): {'values': ['c', '-c'], 'probabilities': [0.45, 0.55]}, ('-a', '-b'): {'values': ['c', '-c'], 'probabilities': [0.6, 0.4]}})
    node4 = Bayesian('D', ['C', 'E'], {('c', 'e'): {'values': ['d', '-d'], 'probabilities': [0.01, 0.99]}, ('c', '-e'): {'values': ['d', '-d'], 'probabilities': [0.5, 0.5]}, ('-c', 'e'): {'values': ['d', '-d'], 'probabilities': [0.75, 0.25]}, ('-c', '-e'): {'values': ['d', '-d'], 'probabilities': [0.31, 0.69]}})
    node5 = Bayesian('E', [], {'values': ['e', '-e'], 'probabilities': [0.35, 0.65]})
    arr = [node1, node5, node2, node3, node4]
    return arr

# Example usage
#network_topology = genbaynetwork()
# for i in range (1000):
#     network_topology = genbaynetwork()
#     sample = priorsample(network_topology)
#     # print("Prior Sample:", sample)
evidence={'C':'-c'}
query={'A':'a'}
evebasedsample=[]
for i in range (1000000):
    network_topology = genbaynetwork()
    sample = priorsample(network_topology)
    for j in evidence:
        if sample[j]==evidence[j]:
            evebasedsample.append(sample)
favout=0
total=len(evebasedsample)
for sam in evebasedsample:
    for item in query:
        if sam[item]==query[item]:
            favout+=1 
print(favout,total)
print("therefore the proabability for p(high income|payment is payback)=",favout/total)