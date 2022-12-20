n , m = map(int,input().split())
a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)
res = []
if n > m:
    dem = 0
    for i in range(n):
        if (i+1)%2 == 1:
            if dem >= n - m :
                res.append(a[i])
            else:
                dem += 1
                continue
        else:
            res.append(a[i])
else:
    for i in range(n):
        tmp = []
        dem = 0
        for j in range(m):
            if (j+1)%2==0:
                if dem >= m - n:
                    tmp.append(a[i][j])
                else:
                    dem += 1
                    continue
            else:
                tmp.append(a[i][j])
        res.append(tmp)
        tmp = []
for i in res:
    for j in i:
        print(j,end = " ")
    print()