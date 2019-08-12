n=int(input(""))
m=list(map(int,input().split()))[0:n]
m.sort(reverse=True)
for i in m:
  print(i)
