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
    if ngto(int(len(n))):
        ngyto , thuong = 0 ,0
        for i in range(len(n)):
            if n[i] == "2" or n[i] == "3" or n[i] == "5" or n[i] == "7" :
                ngyto += 1
            else:
                thuong += 1
        if ngyto > thuong:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1