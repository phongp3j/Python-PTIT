m,n = map(int,input().split())
a = []
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp)
path = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def dq(a,i,j,n,m):
    a[i][j]=0
    for x in path:
        i1 , j1  = i+x[0],j+x[1]
        if n > i1  and m > j1 and i1 >=0   and j1 >=0 and a[i1][j1] == 1:
            dq(a,i1,j1,n,m)
res = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            res += 1
            dq(a,i,j,n,m)
print(res)