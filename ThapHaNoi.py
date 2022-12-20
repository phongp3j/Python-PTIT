def chuyen(n,nguon,tg,dich):
    if n==1:
        print(nguon,"->",dich)
    else:
        chuyen(n-1,nguon,dich,tg)
        chuyen(1,nguon,tg,dich)
        chuyen(n-1,tg,nguon,dich)
n=int(input())
chuyen(n,'A','B','C')