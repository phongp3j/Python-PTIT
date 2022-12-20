t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = [0]*1004
    for i in range(n):
        x = int(input())
        a[x] += 1
    res = 0
    ind = 0
    for i in range(1003):
        if a[i] > res :
            res = a[i]
            ind = i
        elif a[i] == res:
            if ind > i:
                ind = i
    print(ind)