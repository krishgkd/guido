#krish
from itertools import combinations
k,l=input().split()
y=int(y)
x=[]
c=len(k)-l
f=combinations(k,c)
for i in list(f):
  x.append("".join(i))
print(min(x))