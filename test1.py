'''
import random
random_nums=[]
while len(random_nums)!=10:
    x=random.randint(1,100)
    if x not in random_nums:
        random_nums.append(x)
print(random_nums)

add=lambda a,b:a+b
print(add(1,2))
'''
str="rohit"
str=tuple(str)
print(str)

