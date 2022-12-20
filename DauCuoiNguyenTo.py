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
    res1 = n[0] + n[1] + n[2]
    res1 = int(res1)
    res2 = n[len(n)-3] + n[len(n)-2] + n[len(n)-1]
    res2 = int(res2)
    if ngto(res1) and ngto(res2):
        print("YES")
    else:
        print("NO")
    t -= 1