k=int(input())
count=0
for l in range(2,k):
    if(k%l==0):
        count=1
        break
    else:
        count=0
if(count>0):
    print('no')
else:
    print('yes')