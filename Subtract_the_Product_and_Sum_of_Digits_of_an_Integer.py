n=int(input())
s=0
p=1
while n>0:
  t=n%10
  n=n//10
  s+=t
  p*=t
  result=p-s
print(result)