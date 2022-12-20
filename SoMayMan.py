n = int(input())
dem4 ,dem7 = 0 , 0
while n!=0 :
    if n%10 == 4:
        dem4 += 1
    if n%10 == 7:
        dem7 += 1
    n //= 10
if dem4 + dem7 == 4 or dem4 + dem7 == 7:
    print("YES")
else:
    print("NO")