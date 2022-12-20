import math
class mua:
    def __init__(self,ten,bd,kt,luongmua,i):
        self.ten = ten
        self.bd = bd
        self.kt = kt
        self.luongmua = luongmua
        if i < 10:
            self.ma = "T0"+str(i)
        else:
            self.ma = "T"+str(i)
        self.tg = ((ord(kt[0])-48)*10+(ord(kt[1])-48))*60+(ord(kt[3])-48)*10+(ord(kt[4])-48) - (((ord(bd[0])-48)*10+(ord(bd[1])-48))*60+(ord(bd[3])-48)*10+(ord(bd[4])-48))
    def trungbinh(self):
        print("{:.2f}".format(self.luongmua*60/(self.tg)))
t = int(input())
list = []
for i in range(t):
    s1 = str(input())
    s2 = str(input())
    s3 = str(input())
    s4 = int(input())
    a = mua(s1,s2,s3,s4,i+1)
    check = 0
    for k in list:
        if k.ten == a.ten and check == 0:
            check +=1
            k.tg += a.tg
            k.luongmua += a.luongmua
    if check == 0:
        list.append(a)
for i in list:
    print(i.ma,i.ten,sep=" ",end=" ")
    i.trungbinh()