n = str(input())
hoa,thuong = 0, 0
for i in range(len(n)):
    if n[i] >= "A" and n[i]<= "Z":
        hoa+=1
    else:
        thuong += 1
if hoa > thuong:
    print(n.upper())
else:
    print(n.lower())