s1 = str(input())
s2 = str(input())
n = int(input())
res = ""
for i in range(n-1):
    res = res + s1[i]
res = res + s2
for i in range(n-1,len(s1)):
    res = res + s1[i]
print(res)