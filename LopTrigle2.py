import math
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def khoangcach(self,tmp):
        a = self.x - tmp.x
        b = self.y - tmp.y
        return math.sqrt(a*a+b*b)
class tamgiac:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def dientich(self):
        a = self.x.khoangcach(self.y)
        b = self.y.khoangcach(self.z)
        c = self.z.khoangcach(self.x)
        if(max(a,b,c)*2 >= a+b+c):
            print("INVALID")
        else:
            print('{:.2f}'.format(math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4))
a = []
t = int(input())
for i in range(t):
    a += map(float,input().split())
i = 0
for j in range(t):
    tmp = tamgiac(point(a[i],a[i+1]),point(a[i+2],a[i+3]),point(a[i+4],a[i+5]))
    tmp.dientich()
    i+=6