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
    n = str(input())
    tong = 0
    check = 0
    for i in range(len(n)):
        if i%2==0:
            if int(n[i])%2!=0:
                check = 1
                break
            else:
                tong += int(n[i])
        if i%2==1:
            if int(n[i])%2==0:
                check = 1
                break
            else:
                tong += int(n[i])
    if ngto(tong) and check == 0:
        print("YES")
    else:
        print("NO")
    t -= 1