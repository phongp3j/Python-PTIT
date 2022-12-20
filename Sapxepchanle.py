t = int(input())
list = []
c = []
l = []
while True:
    a = [int(x) for x in input().split()]
    list += a
    if len(list) == t:
        break
for i in list:
    if i%2==0:
        c.append(i)
    else:
        l.append(i)
c.sort()
l.sort(reverse=True)
chan,le = 0 ,0
for i in list:
    if i % 2 == 0:
        print(c[chan],end= " ")
        chan+=1
    else:
        print(l[le],end=" ")
        le+=1
