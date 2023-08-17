class depart:
    def __init__(self,dpt):
        self.dpt=dpt
class student(depart):
    def __init__(self,name,dpt):
        super().__init__(dpt)
        self.name=name
    def disp(self):
        print(self.name)
        print(self.dpt)
s=student('rohit','ftca')
s.disp()

