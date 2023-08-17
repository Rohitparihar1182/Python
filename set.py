#set
my_set={1,2,3}
print(my_set)
my_set={1.1,"Rohit",(1,2)}
print(my_set)
my_set={1,2,3,4,3,2}
print(my_set)
print(type(my_set))
my_set={}
print(type(my_set))
my_set=set()
print(type(my_set))
my_set={1,2,3}
#adding elements in a set
my_set.add("Rohit")
print(my_set)
my_set.update([8,5],{4,10,22})
print(my_set)
#deleting element
my_set.discard("Rohit")
print(my_set)
my_set.remove(22)
print(my_set)
