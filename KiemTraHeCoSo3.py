t = int(input())
while t!=0:
    n = str(input())
    check = 0
    for i in range(len(n)):
        if n[i]!="1" and n[i]!="2" and n[i]!="0":
            check = 1
            break
    if check == 1:
        print("NO")
    else:
        print("YES")
    t -= 1