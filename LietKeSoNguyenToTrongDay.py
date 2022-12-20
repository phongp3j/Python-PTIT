import math
a = [True] *(10**6+1)
a[0] = False
a[1] = False
for i in range(2,math.isqrt(10**6+1)):
    if a[i] == True:
        for j in range(2*i,10**6+1,i):
            a[j] = False
n = int(input())
c = list(map(int,input().split()))
b = [0]*(10**6+1)
for i in range(n):
    b[c[i]] += 1
for i in range(n):
    if a[c[i]] and b[c[i]]!=0:
        print(c[i],b[c[i]],sep=" ")
        b[c[i]] = 0