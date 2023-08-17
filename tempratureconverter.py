def farh(cel):
    return (cel*(9/5))+32
def celc(far):
    return (far-32)*(5/9)
print(celc(95))
def sum(n):
    if n==0:
        return n
    else:
        return n+sum(n-1)
print(sum(5))