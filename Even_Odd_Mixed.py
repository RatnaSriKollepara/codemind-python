a=int(input())
e=0
o=0
while a>0:
    b=a%10
    a=a//10
    if b%2==0:
        e+=1
    elif b%2!=0:
        o+=1
if e==0:
    print("Odd")
elif o==0:
    print("Even")
else:
    print("Mixed")
    