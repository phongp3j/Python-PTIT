t = int(input())
a = []
for i in range(t):
    x = str(input())
    a.append(x)
res1 = a[0]
res2 = 0
for i in range(1,t):
    if a[i] == "":
        print(res1,": ",res2,sep="")
        res1 = a[i+1]
        res2 = 0
    else:
        if a[i] == res1:
            continue
        else:
            res2+=1
print(res1,": ",res2,sep="")