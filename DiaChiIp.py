t = int(input())
def check(a):
    if len(a) < 4:
        return False
    else:
        for i in a:
            if i.isdigit():
                if int(i) < 0  or int(i) > 255:
                    return False
            else:
                return False
    return True
while t!=0:
    t-=1
    a = input().split('.')
    if check(a):
        print("YES")
    else:
        print("NO")