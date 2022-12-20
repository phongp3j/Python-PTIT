import itertools
t = int(input())
for i in range(t):
    list1 = []
    n = int(input())
    for i in range(n):
        list1.append(i+1)
    dem = 0
    res = list(itertools.permutations(list1))
    res.reverse()
    print(len(res))
    for i in res:
        for j in i:
            print(j,end="")
        print(end = " ")
    print()