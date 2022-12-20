def doi(a):
    n = 0
    for i in a:
        n = n + ord(i) - ord('0')
    return str(n)
a = str(input())
n = 0
while len(a)>1:
    n+=1
    a = doi(a)
print(n)