a,b=map(int,input().split())
c=list(map(int,input().split()))[:a]
d=0
for i in range(0,len(c)-1):
  for j in range(i+1,len(c)-1):
    if(c[i]+c[j]==b):
      d+=1
if d==1:
  print("yes")
else:
  print("no")
