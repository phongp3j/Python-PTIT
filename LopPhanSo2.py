def GCD(a,b):
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)
class phanSo:
    def __init__(self,tu,mau):
        self.tu = tu/GCD(tu,mau)
        self.mau = mau/GCD(tu,mau)
    def out(self,k):
        self.tu = self.tu*k.mau + k.tu*self.mau
        self.mau = self.mau*k.mau
        tmp = (GCD(self.tu,self.mau))
        self.tu = self.tu/tmp
        self.mau = self.mau/tmp
        print(int(self.tu),int(self.mau),sep="/")
a = input().split()
b = phanSo(int(a[0]),int(a[1]))
c = phanSo(int(a[2]),int(a[3]))
b.out(c)