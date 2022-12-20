t = int(input())
while t!=0:
    t-=1
    n,p = map(int,input().split())
    res = 0
    i = 1
    while p**i <= n:
        res += n//(p**i)
        i+=1
    print(res)