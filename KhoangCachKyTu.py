t = int(input())
while t!=0:
    t-=1
    a = str(input())
    b = []
    for i in a:
        b.append(ord(i))
    c = b[::-1]
    check = 0
    for i in range(1,len(a)):
        if abs(c[i]-c[i-1])!=abs(b[i]-b[i-1]):
            check = 1
            break
    if check!=0:
        print("NO")
    else:
        print("YES")