import math
def ngto(n):
    if n < 2 :
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i == 0:
                return False
    return True
n,m = map(int,input().split())
a = []
res = 0
for i in range(n):
    b = list(map(int,input().split()))
    for c in b:
        if ngto(c) and c > res:
            res = c
    a.append(b)
if res == 0:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print("Vi tri [",i,"][",j,"]",sep ="")