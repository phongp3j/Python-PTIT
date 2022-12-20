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
    res = 0
    for i in range(len(n)):
        if ngto(int(n[i])):
            res += 1
    if ngto(len(n)) and res > len(n) - res:
        print("YES")
    else:
        print("NO")
    t -= 1