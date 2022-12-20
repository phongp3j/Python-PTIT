class thiSinh:
    def __init__(self,ten,ngaysinh,d1,d2,d3):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def out(self):
        f = self.d1+self.d2+self.d3
        print(self.ten,self.ngaysinh,"{:.1f}".format(f),sep=" ")
s1 = str(input())
s2 = str(input())
s3 = float(input())
s4 = float(input())
s5 = float(input())
a = thiSinh(s1,s2,s3,s4,s5)
a.out()