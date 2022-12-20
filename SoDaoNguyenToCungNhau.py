import math
t = int(input())
while t!=0:
    n = int(input())
    tmp1,tmp2 = n , 0
    while n!=0:
        tmp2 = tmp2*10 + n%10
        n//=10
    if math.gcd(tmp1,tmp2) == 1:
        print("YES")
    else:
        print("NO")
    t-=1