from datetime import datetime
class thi:
    def __init__(self,s1,s2,s3,s4):
        if s1 < 10:
            self.ma = "C00"+str(s1)
        elif s1 < 100:
            self.ma = "C0"+str(s1)
        else:
            self.ma = "C"+str(s1)
        self.ngay = s2
        self.gio = s3
        self.phong = s4
        self.time = datetime.strptime(self.ngay+' '+self.gio,'%d/%m/%Y %H:%M')
    def out(self):
        print(self.ma,self.ngay,self.gio,self.phong,sep=" ")
file = open('CATHI.in','r')
list = []
for i in range(int(file.readline())):
    a = thi(i+1,file.readline().strip(),file.readline().strip(),file.readline().strip())
    list.append(a)
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i].time > list[j].time:
            list[i],list[j] = list[j],list[i]
        elif list[i].time == list[j].time :
            if list[i].ma > list[j].ma:
                list[i],list[j] = list[j],list[i]
for i in list:
    i.out()