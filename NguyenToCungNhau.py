import math
a,b = map(int,input().split())
dem = 0
for i in range(10**(b-1),10**(b)):
    if math.gcd(a,i) == 1:
        dem+=1
        if dem%10 == 0 :
            print(i)
        else:
            print(i,end=" ")