class soPhuc:
    def __init__(self,thuc,ao):
        self.thuc = thuc
        self.ao = ao
    def out(self,k):
        x = (self.thuc+k.thuc)*self.thuc-(self.ao+k.ao)*self.ao
        y = (self.thuc+k.thuc)*self.ao+(self.ao+k.ao)*self.thuc
        z = (self.thuc+k.thuc)**2-(self.ao+k.ao)**2
        t = 2*(self.thuc+k.thuc)*(self.ao+k.ao)
        print(x,y,sep=" + ",end="")
        print("i",end=", ")
        print(z,t,sep=" + ",end="")
        print("i")
t = int(input())
while t!= 0:
    t-=1
    a = input().split()
    b = soPhuc(int(a[0]),int(a[1]))
    c = soPhuc(int(a[2]),int(a[3]))
    b.out(c)