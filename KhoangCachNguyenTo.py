import math
a = [True] *(10**6+1)
a[0] = False
a[1] = False
for i in range(2,math.isqrt(10**6+1)):
    if a[i] == True:
        for j in range(2*i,10**6+1,i):
            a[j] = False
n, x = map(int,input().split())
print(x,end = " ")
while n!=0:
    for i in range(10**6+1):
        if a[i]:
            x = x + i
            print(x,end=" ")
            n-=1
            if n== 0 :
                break