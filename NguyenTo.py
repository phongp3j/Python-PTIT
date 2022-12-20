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
    n =int(input())
    dem = 0
    for i in range(1,n):
        if math.gcd(i,n) == 1:
            dem += 1
    if ngto(dem):
        print("YES")
    else:
        print("NO")
    t -= 1 