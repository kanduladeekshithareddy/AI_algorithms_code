import random

class Bayesian:
    def __init__(self, name, parent, cpt):
        self.n = name
        self.p = parent
        self.cpt = cpt

def genrando():
    return random.random()

def weighted_sample(topology, evidence):
    sample={}
    w=1
    while topology:
        t = topology[0]
        topology.pop(0)
        rnum = genrando()
        if t.n in evidence:
            sample[t.n]=evidence[t.n]
            if t.p==[]:
                if evidence[t.n]== t.cpt['values'][0]:
                    w=w*(t.cpt['probabilities'][0])
                else:
                    w=w*(t.cpt['probabilities'][1])
            else:
                parent_values = [sample[parent] for parent in t.p]
                cpt = t.cpt[tuple(parent_values)]
                if evidence[t.n] == cpt['values'][0]:
                    w=w*(cpt['probabilities'][0])
                else:
                    w=w*(cpt['probabilities'][1])
        else:
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

    return sample, w

def generate_bayesian_network():
    node1 = Bayesian('A', [], {'values': ['a', '-a'], 'probabilities': [0.3, 0.7]})
    node2 = Bayesian('B', ['A'], {('a',): {'values': ['b', '-b'], 'probabilities': [0.1, 0.9]}, ('-a',): {'values': ['b', '-b'], 'probabilities': [0.6, 0.4]}})
    node3 = Bayesian('C', ['A', 'B'], {('a', 'b'): {'values': ['c', '-c'], 'probabilities': [0.05, 0.95]}, ('a', '-b'): {'values': ['c', '-c'], 'probabilities': [0.5, 0.5]}, ('-a', 'b'): {'values': ['c', '-c'], 'probabilities': [0.45, 0.55]}, ('-a', '-b'): {'values': ['c', '-c'], 'probabilities': [0.6, 0.4]}})
    node4 = Bayesian('D', ['C', 'E'], {('c', 'e'): {'values': ['d', '-d'], 'probabilities': [0.01, 0.99]}, ('c', '-e'): {'values': ['d', '-d'], 'probabilities': [0.5, 0.5]}, ('-c', 'e'): {'values': ['d', '-d'], 'probabilities': [0.75, 0.25]}, ('-c', '-e'): {'values': ['d', '-d'], 'probabilities': [0.31, 0.69]}})
    node5 = Bayesian('E', [], {'values': ['e', '-e'], 'probabilities': [0.35, 0.65]})
    return [node1, node5, node2, node3, node4]

def likelihood_weighting(topology, evidence, query, num_samples):
    fav_weight = 0
    total_weight = 0

    for _ in range(num_samples):
        sample, weight = weighted_sample(topology, evidence.copy())
        total_weight += weight
        if query.items() <= sample.items():
            fav_weight += weight

    probability = fav_weight / total_weight if total_weight != 0 else 0
    return probability

# Define evidence and query variables
evidence = {'C': '-c'}
query = {'A': 'a'}

# Generate Bayesian network
bayesian_network = generate_bayesian_network()

# Number of samples
num_samples = 10

# Calculate probability using likelihood weighting
result = likelihood_weighting(bayesian_network, evidence, query, num_samples)
print("The probability for P(A='a' | C='-c') =", result)
