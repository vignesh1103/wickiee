a=int(input())
p=list(map(int,input().split()))
d=[1]*a
for i in range(a):
  if(i==0):
    if p[i]>p[i+1]:
       d[i]+=d[i+1]
  else:
    if p[i]>p[i-1]:
       d[i]+=d[i-1]
print(sum(d))
