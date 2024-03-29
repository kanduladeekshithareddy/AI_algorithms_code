def PL_Resolution(KB, alpha):
    def PL_Resolve(ci, cj):
        resolvents = []
        for literal_i in ci:
            for literal_j in cj:
                if literal_i == ('not '+literal_j) or literal_j == ('not '+literal_i):
                    # Compute the resolvent by removing literal_i and literal_j
                    resolvent = [l for l in ci if l != literal_i] + [l for l in cj if l != literal_j]
                    #print(resolvent)
                    resolvent = list(set(resolvent))  # Remove duplicates for factoring
                    resolvents.append(resolvent)
        #print("this is from resolvents:",resolvents)
        return resolvents
    clauses = KB+[[f'not {alpha}']]
    new = []
    while True:
        #print(clauses)
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = PL_Resolve(clauses[i], clauses[j])
                for resolvent in resolvents:
                    if not resolvent:  
                        return True
                    if resolvent not in new:
                        new.append(resolvent)
        if all(clause in clauses for clause in new):
            return False
        clauses.extend(new)

# Example usage:
KB =  [['p' , 'q'],['not p', 'q'],['not q','r']]
alpha = "r"
result = PL_Resolution(KB, alpha)
if result :
   print("alpha is entailed")
else:
   print("no ,alpha can't be entailed")