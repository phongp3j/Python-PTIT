import sys
t = int(input())
while t!=0:
    t-=1
    a = str(input())
    res = -sys.maxsize-1
    tmp = ""
    for i in range(len(a)):
        if a[i]>="0" and a[i]<="9":
            tmp = tmp+a[i]
            continue
        else:
            if tmp !="":
                res = max(res,int(tmp))
            tmp = ""
    if tmp !="":
        res = max(res,int(tmp))
    print(res)