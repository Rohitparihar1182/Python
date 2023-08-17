number=(1,2,3,4)
print(number)
print(type(number))
for i in number:
    print(i)
number=list((number))
number[1]=8
number=tuple(number)
print(number)
def function():
    name=input('enter your name:')
    age=int(input('enter your age:'))
    return(name,age)
A=function()

name,age=A
print("name:",name)
print("age:",age)

  