n=int(input(""))
m=[]
for i in range(0,n):
  a=input()
  m.append(a)
b=[]
for i in zip(*m):
  if(i.count(i[0])==len(i)):
    b.append(i[0])
  else:
    break
print(''.join(b))
