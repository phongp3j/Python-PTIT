import math
def ngto(n):
    if n < 2 :
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i == 0:
                return False
    return True
t = int(input())
while t!= 0:
    n,m = map(int,input().split())
    res = math.gcd(n,m)
    tong = 0
    while res!=0:
        tong += res%10
        res//=10
    if ngto(tong):
        print("YES")
    else:
        print("NO")
    t-= 1