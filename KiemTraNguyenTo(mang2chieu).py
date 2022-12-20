import math
def ngto(n):
    if n < 2 :
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i == 0:
                return False
    return True
n,m=map(int,input().split())
a=[]
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
for i in a:
    for j in i:
        if ngto(j):
            print(1,end = " ")
        else:
            print(0,end=" ")
    print("")