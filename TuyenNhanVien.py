class nhanvien:
    def __init__(self,s1,s2,s3,i):
        self.ten = s1
        if s2 > 10:
            self.lt = s2/10
        else:
            self.lt = s2
        if s3 > 10:
            self.th = s3/10
        else:
            self.th = s3
        self.ma = "TS0"+str(i)
        self.tb = (self.lt+self.th)/2
        if self.tb <5:
            self.xep = "TRUOT"
        elif self.tb < 8:
            self.xep = "CAN NHAC"
        elif self.tb <= 9.5:
            self.xep = "DAT"
        else:
            self.xep = "XUAT SAC"
    def out(self):
        print(self.ma,self.ten,'{:.2f}'.format(self.tb),self.xep,sep =" ")
t = int(input())
list = []
for i in range(t):
    s1 = str(input())
    s2 = float(input())
    s3 = float(input())
    a = nhanvien(s1,s2,s3,i+1)
    list.append(a)
for i in range(t):
    for j in range(i+1,t):
        if list[i].tb < list[j].tb:
            list[i],list[j] = list[j],list[i]
for i in list:
    i.out()