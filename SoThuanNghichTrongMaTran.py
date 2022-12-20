import math
def thuannghich(n):
    b = n
    c = 0
    while n!=0:
        c = c*10 + n%10
        n//=10
    return c == b
n,m = map(int,input().split())
a = []
res = 0
for i in range(n):
    b = list(map(int,input().split()))
    for c in b:
        if thuannghich(c) and c > res and c >=10:
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