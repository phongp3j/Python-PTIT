t = int(input())
while t!=0:
    n = str(input())
    res = 1
    for i in range(len(n)):
        if n[i] == "0":
            continue
        else:
            res *= int(n[i])
    print(res)
    t -= 1