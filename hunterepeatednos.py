n=int(input())
m=list(map(int,input().strip().split()))[:n]
def Repeat(a):
  _size=len(a)
  repeated=[]
  for i in range(_size):
    k=i+1
    for j in range(k,_size):
      if a[i] == a[j] and a[i] not in repeated:
        repeated.append(a[i])
  return repeated
print(*Repeat(m),sep=' ')
