n,k=map(int,input().split())
a=k
s=0
array=[]
array=list(map(int,input().strip().split()))[:n]
for i in range(0,a):
  s=s+array[i]
print(s)
