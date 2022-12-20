m , n ,p = map(int,input().split())
a = []
for i in range(m):
    b = list(map(int,input().split()))
    a.append(b)
dem = 0
for i in range(m*p):
    for j in range(n*p):
        if i < dem*p + m:
            if j < dem*p+n:
                print