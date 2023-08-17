'''
class student:
    def put_data(self):
        self.marks=[]
        self.name=input("enter name")
        for i in range(3):
            marks=int(input(f"enter sub{i+1} marks"))
            self.marks.append(marks)
obj=student()
obj.put_data()
'''
x=int(input("enter a number"))
if x>=0:
    print(x)
else:
    raise TypeError
