s = str(input())
res = 0
tmp = ""
while len(s) > 1:
    for i in range(len(s)//2):
        tmp = tmp + s[i]
    res += int(tmp)
    tmp = ""
    for i in range(len(s)//2,len(s)):
        tmp = tmp + s[i]
    res += int(tmp)
    tmp = ""
    s = str(res)
    res = 0
    print(s)