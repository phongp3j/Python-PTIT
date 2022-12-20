class mon:
    def __init__(self,s1,s2,s3):
        self.ma = s1
        self.ten = s2
        self.ht = s3
    def out(self):
        print(self.ma,self.ten,self.ht,sep = " ")
t = int(input())
list= []
for i in range(t):
    s1 = str(input())
    s2 = str(input())
    s3 = str(input())
    a = mon(s1,s2,s3)
    list.append(a)
list.sort(key = lambda x : (x.ma))
for i in list:
    i.out()