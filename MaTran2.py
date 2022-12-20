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
        if j < n-i-1 :
            tren += a[i][j]
        if j > n-i-1:
            duoi += a[i][j]
chenh = abs(tren - duoi)
if chenh <= k:
    print("YES")
    print(chenh)
else:
    print("NO")
    print(chenh)