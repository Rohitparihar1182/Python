def sub(num1,num2):
    print(num1-num2)
def my_sub(func):
    def inner(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return func(num1,num2)
    return inner
sub=my_sub(sub)
sub(5,78
    
