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
    check = 0
    for i in range(len(n)):
        if ngto(i):
            tmp = int(n[i])
            if ngto(tmp):
                continue
            else:
                check += 1
                break
        else:
            tmp = int(n[i])
            if ngto(tmp):
                check += 1
                break
    if check != 0:
        print("NO")
    else:
        print("YES")
    t -= 1