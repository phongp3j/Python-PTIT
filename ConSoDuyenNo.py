t = int(input())
while t!=0:
    t-=1
    a = str(input())
    a = list(a)
    if a[0] == a[-1]:
        print("YES")
    else:
        print("NO")