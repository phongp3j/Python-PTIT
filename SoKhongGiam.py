t = int(input())
while t!=0:
    n = str(input())
    check = 0
    for i in range(1,len(n)):
        if n[i] < n[i-1]:
            check += 1
            print("NO")
            break
    if check == 0:
        print("YES")
    t -= 1