import math
n = int(input())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
k =int(input())
tren , duoi = 0 , 0
for i in range(n):
    for j in range(len(a[i])):
        if j < i :
            duoi += a[i][j]
        if j > i:
            tren += a[i][j]
chenh = abs(tren - duoi)
if chenh <= k:
    print("YES")
    print(chenh)
else:
    print("NO")
    print(chenh)