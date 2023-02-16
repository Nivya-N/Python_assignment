class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        self.area=self.l*self.w
    def perimeter(self):
        self.p=2*(self.l+self.w)
    def display(self):
        print("Length = ",self.l)
        print("Width = ",self.w)
        print("Area = ",self.area)
        print("Perimeter = ",self.p)
