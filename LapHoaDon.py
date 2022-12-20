class hoadon:
    def __init__(self,s1,s2,s3,i):
        self.ten = s1
        self.cu = s2
        self.moi = s3
        self.so = s3 - s2
        if self.so <=50 :
            self.tien = self.so*100*1.02
        elif self.so <= 100:
            self.tien = (50*100 + (self.so - 50)*150)*1.03
        else:
            self.tien = (50*100+50*150+(self.so-100)*200)*1.05
        if i < 10:
            self.ma = "KH0"+str(i)
        else:
            self.ma = "KH"+str(i)
    def out(self):
        print(self.ma,self.ten,round(self.tien),sep=" ")
t = int(input())
list = []
for i in range(t):
    s1 = str(input())
    s2 = int(input())
    s3 = int(input())
    a = hoadon(s1,s2,s3,i+1)
    list.append(a)
for i in range(t):
    for j in range(i+1,t):
        if list[i].tien < list[j].tien:
            list[i],list[j] = list[j],list[i]
for i in list:
    i.out()