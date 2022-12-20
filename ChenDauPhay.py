n = str(input())
res = ""
dem = 0
i = len(n) - 1
while i >= 0:
    dem += 1
    res = n[i] + res
    if dem % 3== 0 and i!= 0:
        res = "," + res
    i -= 1
print(res)