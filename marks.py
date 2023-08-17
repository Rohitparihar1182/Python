class Bio:
    def detail(self,n):
        self.name=[]
        self.sub1=[]
        self.sub2=[]
        self.sub3=[]
        self.Total=[]
        for i in range(n):
            var=input('enter the name:')
            self.name.append(var)
            marks1=int(input('enter marks of english:'))
            self.sub1.append(marks1)
            marks2=int(input('enter marks of maths:'))
            self.sub2.append(marks2)
            marks3=int(input('enter marks of science:'))
            self.sub3.append(marks3)
            total=int(marks1+marks2+marks3)
            self.Total.append(total)

class Show(Bio):
    def show(self,n):
        for i in range(n):
            print('Hello {} Your marks are:{},{},{} and your total is {}/30'.format(self.name[i],self.sub1[i],self.sub2[i],self.sub3[i],self.Total[i]))

A=Show()
num=int(input('enter the number of students:'))
A.detail(num)
A.show(num)
