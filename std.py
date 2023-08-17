class students:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.Total = []
        self.total = 0
    def enterMarks(self):
        for i in range(3):
            m = int(input("Enter mark in subject{}: ".format(i+1)))
            self.marks.append(m)
            self.total=self.total+m
        self.Total.append(self.total)
            
    def display(self):
        print ("Name: {}             Marks: {}            Total: {}/30".format(self.name,self.marks,self.total))

name=input("enter the name of student:")
s1 = students(name)
s1.enterMarks()
s1.display()
