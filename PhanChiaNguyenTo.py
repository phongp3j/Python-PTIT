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
res = []
for i in range(n):
    if a[i] not in res:
        res.append(a[i])
check = 0
for i in range(len(res)):
    tong1 , tong2 = 0 , 0
    for j in range(i + 1):
        tong1 += res[j]
    for k in range(i+1, len(res)):
        tong2 += res[k]
    if ngto(tong1) and ngto(tong2):
        print(i)
        check = 1
        break
if check == 0:
    print("NOT FOUND")