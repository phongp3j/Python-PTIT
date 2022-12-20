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
    n = str(input())
    res = n[len(n)-4] + n[len(n) -3] + n[len(n) -2]+n[len(n)-1]
    res = int(res)
    if ngto(res):
        print("YES")
    else:
        print("NO")
    t -= 1