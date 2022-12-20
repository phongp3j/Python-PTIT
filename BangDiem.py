class sv:
    def __init__(self,s,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,i):
        self.ten = s
        if i < 10:
            self.ma = "HS0"+str(i)
        else:
            self.ma = "HS"+str(i)
        self.tb =(s1*2.0+s2*2.0+s3+s4+s5+s6+s7+s8+s9+s10)/12.0
        self.tb = round((self.tb*100+1)/100,1)
        if self.tb >= 9.0:
            self.xep = "XUAT SAC"
        elif self.tb >= 8.0:
            self.xep = "GIOI"
        elif self.tb >= 7.0:
            self.xep = "KHA"
        elif self.tb >= 5.0:
            self.xep = "TB"
        else:
            self.xep = "YEU"
    def out(self):
        print(self.ma,self.ten,self.tb,self.xep,sep=" ")
list = []
t = int(input())
for i in range(t):
    s1 = str(input())
    s = [float(i) for i in input().split()]
    a = sv(s1,s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],i+1)
    list.append(a)
for i in range(t):
    for j in range(i+1,t):
        if list[i].tb < list[j].tb:
            list[i],list[j] = list[j],list[i]
        elif list[i].tb == list[j].tb:
            if list[i].ma > list[j].ma:
                list[i],list[j] = list[j],list[i]
for i in list:
    i.out()