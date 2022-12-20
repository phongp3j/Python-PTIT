n = int(input())
a = sorted(list(map(int,input().split())))
for i in range(1,30002):
    if i not in a:
        print(i)
        break