kri,jit1=map(str,input().split())
sat=0
if len(kri)>len(jit1):
  kri,jit1=jit1,kri
i=0
while i<len(kri):
  sat+=(ord(jit1[i])-ord(kri[i]))
  i+=1
for i in range(i,len(jit1)):
  sat+=ord(jit1[i])-ord('a')+1
print(sat)