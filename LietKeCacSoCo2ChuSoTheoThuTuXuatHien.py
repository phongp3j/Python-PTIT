a = str(input())
res1 = []
i = 0
while i+2 <= len(a):
    if int(a[i]+a[i+1]) not in res1:
        res1.append(int(a[i]+a[i+1]))
    i+=2
for i in res1:
    print(i,end= " ")