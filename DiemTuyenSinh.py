class sv:
    def __init__(self,ten,diem,dantoc,khuvuc,i):
        if i < 10:
            self.ma = "TS0"+str(i)
        else:
            self.ma = "TS"+str(i)
        tmp = ""
        a = ten.split()
        for i in a:
            for j in range(len(i)):
                if j == 0:
                    tmp = tmp+i[j].upper()
                else:
                    tmp = tmp+i[j].lower()
            tmp = tmp +" "
        self.ten = tmp
        self.diem = diem
        if dantoc == "Kinh":
            self.tong = self.diem
        else:
            self.tong = self.diem + 1.5
        if khuvuc == 1:
            self.tong = self.tong +1.5
        elif khuvuc == 2:
            self.tong = self.tong + 1.0
        else:
            self.tong = self.tong
        if self.tong >=20.5:
            self.trangthai = "Do"
        else:
            self.trangthai = "Truot"
    def out(self):
        return self.ma+" "+self.ten+"{:.1f}".format(self.tong)+" "+self.trangthai
n = int(input())
list = []
for i in range(n):
    a = str(input())
    b = float(input())
    c = str(input())
    d = int(input())
    e = sv(a,b,c,d,i+1)
    list.append(e)
list = sorted(list, key = lambda x : -x.tong)
for i in list:
    print(i.out())