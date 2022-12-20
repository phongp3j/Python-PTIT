t = int(input())
a = []
while t!=0:
    t-=1
    n = str(input())
    if not n in a:
        a.append(n)
print(len(a))