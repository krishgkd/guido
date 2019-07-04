num,num2=input().split()
KG=abs(len(num)-len(num2))
for i in range(len(num)):
  if len(num2)==1 and num2[i] in num:
   break
  if num[i]!=num2[i]:
   KG+=1
print(KG)