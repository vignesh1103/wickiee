a,b=map(int,input().split())
c=list(map(int,input().split()))
e=[]
for i in range(0,b):
  f=[]
  f=list(map(int,input().split()))
  g=c[f[0]-1]
  for j in range(min(f),max(f)):
    g=g^c[j]
  e.append(g)
for i in range(0,len(e)):
  print(e[i])
