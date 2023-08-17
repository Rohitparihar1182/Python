def num():
    number=int(input("enter the number of students"))
    return number
def getdata():
    name=input("enter your name") 
    roll=int(input("enter roll no"))
    course=input("enter your course")
    return(name,roll,course)
def printdata(name,roll,course):
    print("name=",name)
    print("roll no=",roll)
    print("course=",course)
