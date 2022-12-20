t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(10**6+1)
    for i in a:
        b[i]+=1
    res = 0
    for i in range(10**6+1):
        if b[i]>res and b[i]>n/2:
            res = i
    if res == 0:
        print("NO")
    else:
        print(res)