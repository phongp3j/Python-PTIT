t = int(input())
while t!=0:
    n = str(input())
    if n[len(n)-1] == "6" and n[len(n)-2] == "8":
        print("YES")
    else:
        print("NO")
    t-=1