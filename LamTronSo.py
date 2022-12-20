t = int(input())
while t!=0:
    t-=1
    n = int(input())
    nho = 0
    res = ""
    while n>=10:
        if n%10 + nho>= 5:
            tmp = "0"
            nho = 1
            res = tmp + res
            n//=10
        else:
            tmp = "0"
            nho = 0
            res = tmp + res
            n//=10
    res = str(n + nho) + res
    print(res)