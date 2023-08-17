'''
def factorial(a):
    f=1
    for i in range(a,1,-1):
        f=f*i
    return f
num=int(input("enter the number:"))
if num<0:
    print("Sorry factorial does not exist for negative number")
elif num==0:
    print("the factorial pf given number is:1")
else:
    print("The factorial of given number is:",factorial(num))






def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
        
num=recur_factorial(8)
print(num)
'''