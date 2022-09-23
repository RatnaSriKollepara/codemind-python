n=int(input())
sq=n*n
sum=0
while sq>0:
    s=sq%10
    sq=sq//10
    sum+=s
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")