n = int(input())
a = []
res = [0]*201
while n!=0:
    b = list(map(int,input().split()))
    for i in b:
        a.append(i)
        res[i] = 1
    n -= len(b)
amax = max(a)
check  = 0
for i in range(1,201):
    if res[i] == 0 and i < amax:
        check = 1
        print(i)
if check == 0:
    print("Excellent!")