a,b=map(int,input().split())
for i in range(a,b):
  s=0
  temp=i
  while(temp>0):
    digit=temp%10
    s+=digit**3
    temp=temp//10

  if i==s:
    print(i,'',end='')
