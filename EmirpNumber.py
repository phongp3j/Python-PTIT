import math
def ngto(n):
    if n < 2 :
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i == 0:
                return False
    return True
def dao(n):
    res = 0
    while n!=0:
        res = res*10+n%10
        n//=10
    return res
t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = [True]*(10**6+1)
    for i in range(n):
        if ngto(i) and a[i] and ngto(dao(i)) and i!=dao(i) and dao(i)<=n:
            print(i,dao(i),end = " ")
            a[i] = False
            a[dao(i)] = False
    print("")