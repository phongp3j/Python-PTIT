class Rectangle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z.title()
    def check(self):
        if self.x <= 0 or self.y <= 0:
            return 0
        return 1
    def out(self):
        if self.check()==1:
            print((self.x+self.y)*2,self.x*self.y,self.z,sep=" ")
        else:
            print("INVALID")
a = input().split()
b = Rectangle(int(a[0]),int(a[1]),str(a[2]))
b.out()