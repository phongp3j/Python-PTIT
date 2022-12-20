n , m = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*12
for i in range(n):
    b[a[i]] += 1
res1 , res2 = 0 , 0
for i in range(m+1):
    if b[i] > b[res1]:
        res2 = res1
        res1 = i
    if b[i] < b[res1] and b[i] > b[res2]:
        res2 = i
if res2 == 0:
    print("NONE")
else:
    print(res2)