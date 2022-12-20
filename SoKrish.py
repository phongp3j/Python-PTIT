t = int(input())
def giaithua(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res
while t!=0:
    t-=1
    n = str(input())
    b = int(n)
    n = list(n)
    res = 0
    for i in n:
        res += giaithua(int(i))
    if res == b:
        print("Yes")
    else:
        print("No")
