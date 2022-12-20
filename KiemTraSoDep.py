t = int(input())
while t!=0:
    t-=1
    check = True
    n = str(input())
    for i in range(len(n)-2):
        if n[i]!=n[i+2] or n[i] == n[i+1]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")