class gv:
    def __init__(self,ten,ma,tin,chuyen,i):
        if i < 10:
            self.mgv = "GV0"+str(i)
        else:
            self.mgv = "GV"+str(i)
        self.ten = ten
        self.ma = ma
        self.tin = tin
        self.chuyen = chuyen
        if ma[0] == "A":
            self.mon = "TOAN"
        elif ma[0] == "B":
            self.mon = "LY"
        else:
            self.mon = "HOA"
        if ma[1] == "1":
            self.tong = tin*2+chuyen+2.0
        elif ma[1] == "2":
            self.tong = tin*2+chuyen+1.5
        elif ma[1] == "3":
            self.tong = tin*2+chuyen+1.0
        else:
            self.tong = tin*2 + chuyen
        if self.tong >= 18:
            self.ketqua = "TRUNG TUYEN"
        else:
            self.ketqua = "LOAI"
    def out(self):
        return self.mgv + " " +self.ten + " "+ self.mon + " "+ "{:.1f}".format(self.tong)+" "+self.ketqua
    
n = int(input())
list = []
for i in range(n):
    a = str(input())
    b = str(input())
    c = float(input())
    d = float(input())
    e = gv(a,b,c,d,i+1)
    list.append(e)
list = sorted(list, key = lambda x : -x.tong)
for i in list:
    print(i.out())