def hcf(num1,num2):
    if num1>num2:
        lower=num2
    else:
        lower=num1
    for i in range(1,lower+1):
        if (num1%i==0) & (num2%i==0):
            hcf=i
    return hcf
print(hcf(24,58))
def lcm(num1,num2):
    if num1>num2:
        upper=num2
    else:
        upper=num1
    