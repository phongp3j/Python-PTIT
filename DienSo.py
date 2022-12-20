t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a  = list(map(int,input().split()))
    amin = min(a)
    amax = max(a)
    b = []
    for i in range(len(a)):
        if a[i] not in b :
            b.append(a[i])
    res = amax - amin + 1 - len(b)
    print(res)