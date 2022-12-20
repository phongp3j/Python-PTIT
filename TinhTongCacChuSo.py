t = int(input())
while t!=0:
    n = str(input())
    tong = 0
    res = ""
    for i in range(len(n)):
        if n[i]>="0" and n[i]<="9":
            tong += int(n[i])
        else:
            res = res + n[i]
    res1 = sorted(res)
    res1 = join(res1)
    print(res1,end="")
    print(tong)
    t-=1