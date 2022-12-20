t = int(input())
while t!= 0:
    n = str(input())
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    if res%3 == 0:
        print("YES")
    else:
        print("NO")
    t -= 1