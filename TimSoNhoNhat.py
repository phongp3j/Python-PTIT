import sys
t = int(input())
while t!=0:
    t-=1
    a = str(input())
    res = sys.maxsize
    tmp = ""
    for i in range(len(a)):
        if a[i]>="0" and a[i]<="9":
            tmp = tmp+a[i]
            continue
        else:
            if tmp !="":
                res = min(res,int(tmp))
            tmp = ""
    print(res)