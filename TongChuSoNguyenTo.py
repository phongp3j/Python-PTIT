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
       res += int(n[i])
    if ngto(res):
        print("YES")
    else:
        print("NO")
    t -= 1