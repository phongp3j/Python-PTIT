while True:
    n = int(input())
    if n == 0:
        break
    res = []
    res1 = 1
    while n!=1:
        if n%2 == 0:
            if n%2 not in res:
                res.append(n//2)
                res1+=1
            n//=2
        else:
            if n*3+1 not in res:
                res.append(n*3+1)
                res1+=1
            n = n*3+1
    print(res1)