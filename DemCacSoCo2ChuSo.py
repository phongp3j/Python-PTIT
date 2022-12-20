a = str(input())
res1 = []
res2 = [0]*(10**4+1)
i = 0
while i+2 <= len(a):
    res2[int(a[i]+a[i+1])]+=1
    if int(a[i]+a[i+1]) not in res1:
        res1.append(int(a[i]+a[i+1]))
    i+=2
for i in res1:
    print(i,res2[i])