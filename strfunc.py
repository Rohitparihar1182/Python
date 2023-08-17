'''myset=set()
for i in range(0,7,1):
    myset.add(i+1)
print(myset)
myset.clear()
myset.add(18)
myset.add("18")
print(myset)

name=[]
favlang=[]
for i in range(4):
    var=input("enter your name ")
    name.append(var)
    var=input("enter your favourite language ")
    favlang.append(var)
D={"name":name,"favlanguage":favlang}
print(D)


marks=[]
total=0
for i in range(3):
    print(f"enter sub{i+1} marks")
    mark=int(input())
    marks.append(mark)
    total+=mark
total/=3
if total>40:
    for i in range(3):
        if marks[i]<33:
            print("you are fail,better luck next time")
            break
else:
    print("you are fail,better luck next time")


text=input('enter the text')
if("subscribe this" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("make a lot of money" in text):
    spam=True
else:
    spam=False
if(spam):
    print("this text is spam")
else:
    print("this text is not spam")


l1=["aman","rohit","sumit","gourav","gale","yogi"]
name=input("enter your name to search")
if(name in l1):
    print("you are selected")
else:
    print("you are not selected")
'''




s="riohit"
s.upper()
print(s.upper())









    
