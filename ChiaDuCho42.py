t = 10
res = []
while t!=0:
    a = list(map(int,input().split()))
    t-=len(a)
    for i in range(len(a)):
        if a[i]%42 in res:
            continue
        else:
            res.append(a[i]%42)
print(len(res))