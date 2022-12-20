import math
t = int(input())
while t!=0 :
    t-=1
    n = int(input())
    print("1",end = "")
    for i in range(2,math.isqrt(n)+1):
        dem = 0
        while n%i==0:
            dem+=1
            n//=i
        if dem!=0:
            print(" * "+ str(i) + "^" + str(dem),end="")
    if n>1:
        print(" * " + str(n)+"^1")
    print(end = "\n")