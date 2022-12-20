t = int(input())
def thuannghich(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
while t!= 0:
    n = str(input())
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    if res >= 10 and thuannghich(res):
        print("YES")
    else:
        print("NO")
    t -= 1