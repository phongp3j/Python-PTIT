import math
n , m = map(int,input().split())
a = []
minres , maxres = 10001 , -1
for i in range(n):
    b = list(map(int,input().split()))
    minres = min(min(b),minres)
    maxres = max(max(b),maxres)
    a.append(b)
res = maxres - minres
check = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == res:
            if check == 0:
                print(res)
            print("Vi tri [",i,"][",j,"]",sep = "")
            check = 1
if check == 0:
    print("NOT FOUND")