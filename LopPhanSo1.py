def GCD(a,b):
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)
class phanSo:
    def __init__(self,tu,mau):
        self.tu = tu/GCD(tu,mau)
        self.mau = mau/GCD(tu,mau)
    def out(self):
        print(int(self.tu),int(self.mau),sep="/")
a = input().split()
b = phanSo(int(a[0]),int(a[1]))
b.out()
    