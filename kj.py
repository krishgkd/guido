kk = int(input())
m=[]
for i in range(0,kk):
 inpu=input()
 m.append(inpu)
li=[]
for i in zip(*m):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))