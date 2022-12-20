n = int(input())
a = []
for i in range(n):
    s = list(map(str,input().split()))
    a.append(len(s))
res = 0
res1 = []
i = 0
while i < n:
    if a[i] == 7:
        res +=1
        res1.append(2)
        i+=4
        if i == n -1:
            break
    else:
        while a[i] != 7:
            i+=1
            if i == n -1:
                break
        res+=1
        res1.append(1)
        if i == n -1:
            break
print(res)
for i in res1:
    print(i)