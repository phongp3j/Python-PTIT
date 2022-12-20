n = int(input())
a = []
tmp = ""
while n!=0:
    n-=1
    s=str(input())
    i = 0
    while i < len(s):
        if s[i].isdigit():
            tmp += s[i]
            i+=1
        else:
            if tmp!="":
                a.append(int(tmp))
            tmp = ""
            i+=1
    if tmp!="":
        a.append(int(tmp))
    tmp = ""
if tmp!="":
    a.append(int(tmp))
a = sorted(a)
for i in a:
    print(i)