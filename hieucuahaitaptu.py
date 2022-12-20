t = int(input())
for i in range(t):
    n = str(input())
    c , l = 0 ,1 
    for i in range(len(n)):
        if i%2==0:
            if n[i]!='0':
                l *= (ord(n[i])-48)
        else:
            c += (ord(n[i])-48)
    if c==0:
        print("INVALID")
    else:
        print("{:.6f}".format(l/c))