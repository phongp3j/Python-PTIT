t = int(input())
a = {}
b = []
for i in range(t):
    arr = [x.lower() for x in input().split("[]")]
    b += arr
    for j in arr:
        if j in a:
            a[j] += 1
        else:
            a[j] = 1
b = list(set(b))
b.sort(key = lambda x : (-a[x] , x))
for i in b:
    print(i, a[i])