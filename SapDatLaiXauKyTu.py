t = int(input())
test = t
while t!=0:
    t-=1
    a = sorted(str(input()))
    b = sorted(str(input()))
    if a==b:
        print("Test ", test - t, ": YES",sep="")
    else:
        print("Test ", test - t, ": NO",sep="")