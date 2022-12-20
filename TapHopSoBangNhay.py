n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1 = {}
for i in range(n):
    a1[a[i]] = 1
b1 = {}
for i in range(m):
    b1[b[i]] = 1
sorted(a1)
sorted(b1)
if len(a1) == len(b1):
    check = 0
    for i in a1:
        if a1[i] != b1[i]:
            check = 1
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")