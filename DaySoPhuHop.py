t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    check = True
    for i in range(n):
        if a[i] > b[i]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")