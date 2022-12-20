t = int(input())
while t!=0:
    n = str(input())
    if len(n) % 2 == 0 or n[0] == n[1]:
        print("NO")
    else:
        check = 0
        for i in range(2,len(n),2):
            if n[i]!=n[i-2]:
                check +=1
                break
        if check!=0:
            print("NO")
        else:
            print("YES")
    t -= 1