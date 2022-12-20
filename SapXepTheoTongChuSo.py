import math
def tong(n):
    res = 0
    while n!=0:
        res += n%10
        n//=10
    return res
def item(n):
    return tong(n),n
t = int(input())
while t!=0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key = item)
    for i in a:
        print(i,end=" ")
    print("")