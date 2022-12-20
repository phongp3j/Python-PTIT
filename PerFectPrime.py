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
    if ngto(n):
        res = 0
        sum1 = 0
        check = 0
        while n!=0:
            res = res*10+n%10
            sum1 = sum1+n%10
            if ngto(n%10) == False:
                check = 1
                break
            n//=10
        if ngto(res) and ngto(sum1) and check == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")