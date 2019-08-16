def main(S,R,C):
  sum=(S/2)*(2*R+(S-1)*C)
  return sum
S,R,C=map(int,input().split())
print(int(main(S,R,C)))
