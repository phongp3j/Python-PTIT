n = int(input())
a = list(map(int,input().split()))
b = []
b.append(a[0])
for i in range(1,n):
    if len(b)!=0:
        if (b[len(b)-1] + a[i])%2==0:
            b.pop()
        else:
            b.append(a[i])
    else:
        b.append(a[i])
print(len(b))