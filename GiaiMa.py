t = int(input())
while t!=0:
    n = str(input())
    res = ""
    for i in range(len(n)):
        if n[i] >= "1" and n[i]<="9":
            dem = int(n[i])
            while dem!=0:
                res = res + n[i-1]
                dem -= 1
    print(res)
    t -= 1