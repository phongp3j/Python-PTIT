class sv:
    def __init__(self,ten,d1,d2,d3,i):
        if i < 10:
            self.ma = "SV0"+str(i)
        else:
            self.ma = "SV"+str(i)
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
        self.tong = (d1*3+d2*3+d3*2)/8
        self.rank = None
    def out(self):
        return self.ma+" "+self.ten+'{:.2f}'.format(self.tong+0.001)+" "+str(self.rank)
n = int(input())
list = []
for i in range(n):
    a = str(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = sv(a,b,c,d,i+1)
    list.append(e)
list = sorted(list, key = lambda x : -x.tong)
list[0].rank = 1
for i in range(1,n):
    if list[i].tong == list[i-1].tong:
        list[i].rank = list[i-1].rank
    else:
        list[i].rank = i+1
for i in list:
    print(i.out())