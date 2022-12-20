import math

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def khoangCach(self,tmp):
        res1 = self.x - tmp.x
        res2 = self.y - tmp.y
        res = math.sqrt(res1*res1 + res2*res2)
        return res
class tamgiac:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def chuvi(self):
        a = self.x.khoangCach(self.y)
        b = self.y.khoangCach(self.z)
        c = self.z.khoangCach(self.x)
        if(max(a,b,c)*2 >= a+b+c):
            print("INVALID")
        else:
            print("{:.3f}".format(a+b+c))
a= []
t =int(input())
t1= t
while t!= 0:
    a+= map(float,input().split())
    t-=1
i = 0
for j in range(t1):
    tmp = tamgiac(point(a[i],a[i+1]),point(a[i+2],a[i+3]),point(a[i+4],a[i+5]))
    tmp.chuvi()
    i+=6