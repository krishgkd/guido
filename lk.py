k = int(input())
l = list(map(int,input().split()))
l.sort()
j = []
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        j.append(t[i])
if j:
    for x in set(j):
        print(x,end=" ")
else:
    print("unique")