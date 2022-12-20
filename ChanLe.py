t = int(input())
while t!=0:
    t-=1
    n = int(input())
    tmp = str(n)
    tong = 0
    while n!=0:
        tong += n%10
        n//=10
    if tong%10==0:
        check = 0
        for i in range(len(tmp)-1):
            if abs(int(tmp[i]) - int(tmp[i+1]))!=2:
                check+=1
                break
        if check!=0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")