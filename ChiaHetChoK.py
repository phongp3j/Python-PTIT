a , k , n = map(int,input().split())
check = 0
res = 1
while res*k <= a:
    res += 1
for i in range(res*k-a,n-a+1,k):
    if (a+i)%k == 0:
        print(i,end = " ")
        check += 1
if check == 0:
    print(-1)