class number:
    def __init__(self,a):
        self.a=a
    def is_negative(self):
        if self.a<0:
            print("given number is negative")
        else:
            print("given number is not negative")
    def is_divisible(self,x):
        self.x=x
        if self.a%self.x==0:
            print("{} is divisible to {} ".format(self.a,self.x))
        else:
            print("{} is not divisible to {} ".format(self.a,self.x))

N=number(10)
N.is_negative()
N.is_divisible(5)

