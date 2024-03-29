l=[1,2,3,4,5,6,7,5]
l[0]=56 # i can manipulate list  hence mutable
print (l[0:8])
print(l[0:8:2])
l.sort()
print(l)
l.reverse()
print(l)
l.append(-1)
print(l)
l1=l.copy()
l1.sort();
l1.insert(5,10)
l1.remove(5)
l1.pop(0)
l1.sort()
l1.clear()
print(l1)

# entered by usesr create a list

'''
p=[]
for i in range(5):
    t=int(input("enter the number:"))
    p.append(t)
    
print(p)
'''

#tuples
t=(1,1,1,1,1,1,1,1,1,1,1,1,1,5,10,11,34)
print(t[0])
# set[0]=2 tuples cannot be manipulated hence immutable 
print(t)
print(t.count(1))
print(t.index(11)) #the elemnet at index 15


#dictionary

dict={
    "explore":"find something new",
    "lucid":"very clear",
    "anomaly":"unexpected",
    "erudite":"great knowledge",
    "abnegation":"reject",
    "dauntless":"showing fearless",
    "amity":"the kind",
    "candour":"the honest",
    1:"number"
}
print(dict)
print(dict['amity'])
print(dict.keys())
print(dict.values())
print(dict.get('dauntless'))
print(dict.pop(1))
print(list(dict.items())) #dict_items is type casted to lists for iteration
andi={
    "deep":"deeksh",
    "siblings":"forever"
}
dict.update(andi)

print (dict)

#sets

s={1,34,5,6,4,7,23,4}
print(s)
s.add(23)
s.add(9)
print(len(s))
s.remove(34)
s.pop()
s=s.union({34,1})
print(s)
s=s.intersection({8,23,4,5,1})
print(s)
# print(s[0])
#5:18