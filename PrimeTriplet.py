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
while t!=0:
    t-=1
    n = int(input())
    res = 0
    for i in range(2,n+1):
        if ngto(i):
            if (ngto(i+2) and ngto(i+6) and i+2 < n and i+6<n) or (ngto(i+4) and ngto(i+6) and i+4 < n and i+6 < n):
                res += 1
    print(res)