n = str(input())
res = ""
for i in range(len(n)):
    res = res + str(n[i])
    if n[i] == " ":
        print(res)
        res = ""
print(res)