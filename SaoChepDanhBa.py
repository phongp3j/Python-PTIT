class dt:
    def __init__(self,s1,s2,s3):
        self.ngay = s1.split("Ngay ")
        self.ten = s2
        self.dt = s3
    def out(self):
        print(self.ten,": ",end = "")
        print(self.dt,self.ngay,sep=" ")
f = open("SOTAY.txt",'r')
list = f.readlines()
res = []
i = 0
while i < len(list):
    a = dt(list[i].strip(),list[i+1].strip(),list[i+2].strip())
    res.append(a)
    i+=3
res.sort(key = lambda x : (x.ten))
for i in res:
    i.out()