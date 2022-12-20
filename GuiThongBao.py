t = int(input())
while t!=0:
    t-=1
    a = list(map(str,input().split()))
    check = 0
    for i in a:
        check = check + len(i) + 1
        if check > 100:
            break
        print(i,end = " ")
    print()