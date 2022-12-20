t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a.sort()
    b.sort()
    c.sort()
    i,j,k=0,0,0
    res=[]
    while i<x and j<y and k<z:
        if a[i]==b[j] and b[j]==c[k]:
            res.append(a[i])
            i+=1
            j+=1
            k+=1
        elif a[i]<b[j] and a[i]<c[k]: i+=1
        elif b[j]<a[i] and b[j]<c[k]: j+=1
        elif a[i]==b[j] and a[i]<c[k]:
            i+=1
            j+=1
        elif b[j]==c[k] and b[j]<a[i]:
            j+=1
            k+=1
        elif a[i]==c[k] and a[i]<b[j]:
            i+=1
            k+=1
        else:k+=1
    for i in res:print(i,end=" ")
    if len(res)==0:print("NO",end="")
    print()