t = int(input())
while t!=0 :
    t-=1
    s = str(input())
    dem = 1
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            print(dem,s[i-1],sep = "",end = "")
            dem = 1
        else:
            dem+=1
    print(dem,s[len(s)-1],sep="")