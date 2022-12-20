t = int(input())
def thuannghich(n):
    s = str(n)
    if len(s)%2 != 0:
        return False
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1] or int(s[i])%2!=0 or int(s[len(s)-1-i])%2!=0:
            return False
    return True
while t!= 0:
    n = int(input())
    for i in range(22,n,2):
        if thuannghich(i):
            print(i,end = " ")
    print("")
    t -= 1