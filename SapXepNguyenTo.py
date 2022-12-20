import math
def ngto(n):
    if n < 2 :
        return False
    else:
        for i in range(2,math.isqrt(n)+1):
            if n%i == 0:
                return False
    return True
n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n):
    if ngto(a[i]):
        b.append(a[i])
b.sort()
j = 0
for i in range(n):
    if ngto(a[i]):
        a[i] = b[j]
        j+=1
for i in a:
    print(i,end=" ")