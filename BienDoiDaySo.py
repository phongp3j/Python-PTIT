def check(a):
    return a[0] == a[1] and a[1] == a[2] and a[2] == a[3]
while True:
    a = list(map(int,input().split()))
    res = 0
    if check(a) and a[0] == 0:
        break
    else:
        while check(a) == False:
            res+=1
            tmp = a[0]
            a[0] = abs(a[0] - a[1])
            a[1] = abs(a[1] - a[2])
            a[2] = abs(a[2] - a[3])
            a[3] = abs(a[3] - tmp)
        print(res)