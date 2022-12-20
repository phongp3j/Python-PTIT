t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(10**6+1)
    for i in range(n):
        b[a[i]]+=1
    for i in range(n):
        if b[a[i]]%2==1:
            print(a[i])
            break