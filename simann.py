import random,math,time
class Queennode:
    def __init__(self,mat):
        self.pos=mat
    def objective(self):
        count=0
        for i in range(0,8):
            for j in range(i+1,8):
                if self.pos[i]==self.pos[j] or abs(j-i)==abs(self.pos[j]-self.pos[i]):
                   count+=1
        return count
    def successors(self):
        i=random.randrange(8)
        j=random.randrange(8)
        mat=self.pos
        mat[i]=j
        p=Queennode(mat)
        return p
def simulatedannealing(init,exectime):
    t=4000
    sch=0.99
    current=Queennode(init)
    starttime=time.time()
    while time.time()-starttime<exectime:
        T=t*sch
        next=current.successors()
        if t==0:
           return current
        if next.objective()==0:
           return next
        deltae=current.objective()-next.objective()
        prob=(math.e)**(deltae/T)
        if deltae>0 or 0<prob<1:
           current=next
    return None
if __name__ == "__main__":
   mat=[4,2,7,3,1,6,0,5]
   starttime=time.time()
   res=simulatedannealing(mat,10)
   endtime=time.time()
   if res==None:
      print("no solution")
   else:
      print(res.pos)
   print("timetaken:",(endtime-starttime))
   
