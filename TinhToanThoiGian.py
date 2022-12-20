class may:
    def __init__(self,ma,ten,vao,ra):
        self.ma = ma
        self.ten = ten
        self.vao = vao[0]*60+vao[1]
        self.ra = ra[0]*60+ra[1]
        self.tg = self.ra - self.vao
    def out(self):
        print(self.ma,self.ten,int(self.tg/60),"gio",self.tg%60,"phut",sep=" ")
t = int(input())
list = []
for i in range(t):
    s1 = str(input())
    s2 = str(input())
    s3 = [int(i) for i in input().split(':')]
    s4 = [int(i) for i in input().split(':')]
    a = may(s1,s2,s3,s4)
    list.append(a)
for i in range(t):
    for j in range(i+1,t):
        if list[i].tg < list[j].tg:
            list[i],list[j] = list[j],list[i]
        elif list[i].tg == list[j].tg:
            if list[i].ma > list[j].ma:
                list[i],list[j] = list[j],list[i]
for i in list:
    i.out()