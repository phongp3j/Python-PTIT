t = int(input())
f = [0]*100
f[0] = 1
f[1] = 1
for i in range(2,100):
    f[i] = f[i-1] + f[i-2]
while t!=0:
    t-=1
    n , m = map(int,input().split())
    for i in range(n,m+1):
        print(f[i-1],end= " ")
    print(end = "\n")