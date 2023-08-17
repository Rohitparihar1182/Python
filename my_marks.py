class Name:
    def __init__(self,n):
        self.n=n
                   
    def name(self):
        self.name=[]
        self.marks=[]
        self.total=[]
        for i in range(self.n):
            self.subject=[]
            name=input("enter the name:")
            self.name.append(name)
            for j in range(3):
                
                var=int(input(f'{name} enter your subject {j+1} marks:'))
                self.subject.append(var)
            self.marks.append(self.subject)
            total=self.subject[0]+self.subject[1]+self.subject[2]
            self.total.append(total)
class Student(Name):
    def __init__(self,n):
        super().__init__(n)
    def detail(self):
        for i in range(self.n):
            print(f'''{self.name[i]}'s marks:- {self.marks[i]} total: {self.total[i]}''')
n=int(input("enter the number of students:"))
obj=Student(n)
obj.name()
obj.detail()
