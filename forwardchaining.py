def plfc(KB,query):
    count={}
    inferred={}
    agenda=['a','b'] #initial true values
    for clause in KB:
       for symbol in clause['c']:
              count[symbol]=len(clause['p'])
              inferred[symbol]=False
       for symbol in clause['p']:
           inferred[symbol]=False
    while agenda:
        x=agenda.pop(0)
        if x==query:
           return True
        if inferred[x]==False:
           inferred[x]=True
           for clause in KB:
               if 'c' in clause and x in clause['p']:
                  count[clause['c']]-=1
                  if count[clause['c']]==0:
                     agenda.append(clause['c'])
    return False
        
KB=[{'p':['p'],'c':'q'},
    {'p':['l','m'],'c':'p'},
    {'p':['b','l'],'c':'m'},
    {'p':['a','p'],'c':'l'},
    {'p':['a','b'],'c':'l'}]
query='q'
res=plfc(KB,query)
if res:
    print("it is inferred by forward chaining")
else:
    print("it is not inferred")