import rectangle
#r1=rectangle.rectangle(5,20)
#r1.area()
#r1.perimeter()
#r1.display()

class parallelepiped(rectangle.rectangle):
    def __init__(self,l,w,h):
        rectangle.rectangle.__init__(self,l,w)
        #self.l=l
        #self.w=w
        self.h=h
    def volume(self):
        self.v= self.l*self.w*self.h
        return self.v
        

p1=parallelepiped(10,20,2)
p1.area()
p1.perimeter()
p1.display()
print("Volume of parallelepiped = ",p1.volume())