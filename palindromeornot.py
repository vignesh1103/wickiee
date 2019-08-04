a=int(input(""))
b=a
c=0
while(b!=0):
  c=(c*10)+(b%10)
  b=b//10
if (a==c):
  print("yes")
else:
  print("no")
