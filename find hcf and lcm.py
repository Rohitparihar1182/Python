
def hcf(num1,num2):
    if num1<num2:
        lower=num2
        num2=num1
        num1=lower
    while num2!=0:
        num1,num2=num2,num1%num1
    return num1
print(hcf(100,200))

def lcm(num1,num2):
    lcm=num1*num2/hcf(num1, num2)
    return lcm
print(lcm(100,200))

x=100
factor=[]
for i in range(1,x+1):
    if x%(i)==0:
        factor.append(i)
print("factors of ",x,"=",factor)
