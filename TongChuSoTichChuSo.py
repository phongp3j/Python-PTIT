t = int(input())
while t!=0:
    t-=1
    n=str(input())
    tong,tich = 0 , 1
    check = 0
    for i in range(len(n)):
        if i % 2 ==0 :
            tong += int(n[i])
        else:
            if n[i]!="0":
                check += 1
                tich *= int(n[i])
    if check == 0:
        print(tong,0,sep =" ")
    else:
        print(tong,tich,sep=" ")