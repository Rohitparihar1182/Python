class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def perimeter(self):
        if self.a+self.b<=self.c:
            print("invalid input: make sure a+b>c")
        elif self.c+self.b<=self.a:
            print("invalid input: make sure b+c>a")
        elif self.a+self.c<=self.b:
            print("invalid input: make sure a+c>b")
        else:
            self.p=self.a+self.b+self.c
            print("The perimeter of the triangle is:",self.p)

    def area(self):
        if self.a+self.b<=self.c:
            print("can not find area: make sure a+b>c")
        elif self.c+self.b<=self.a:
            print("can not find area: make sure b+c>a")
        elif self.a+self.c<=self.b:
            print("can not find area: make sure a+c>b")
        else:
            self.s=self.p/2
            x=self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)
            x=x**0.5
            print("The area of triangle is:",x)
        
        
t=triangle(4,15,13)
t.perimeter()
t.area()



