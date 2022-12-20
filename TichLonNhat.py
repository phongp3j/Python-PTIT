n = int(input())
a = sorted(list(map(int,input().split())))
res  = max(a[0]*a[1]*a[2],a[n-1]*a[n-2]*a[n-3],a[0]*a[1],a[n-1]*a[n-2],a[0]*a[1]*a[n-1])
print(res)