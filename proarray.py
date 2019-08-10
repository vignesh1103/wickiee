n=int(input())
li=list(map(int,input().split()))
m=0
for i in range(1,len(li)):
  if (sum(li[:i]))//len(li[:i])==(sum(li[i:]))//len(li[i:]):
    m+=1
  else:
    m=0
if m>=1:
  print("yes")
else:
  print("no")
