while True:
    n = int(input())
    if n==0:
        break
    else:
        a = []
        for i in range(n):
            x = int(input())
            a.append(x)
        res1 = min(a)
        res2 = max(a)
        if res1==res2:
            print("BANG NHAU")
        else:
            print(res1,res2,sep=" ")