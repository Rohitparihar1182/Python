my_dict={}
my_dict={'name':'Rohit','roll':2}
d1=dict({1:'Rohit',2:'Parihar'})
print(my_dict['name'])
print(d1[1])
d1['mid_name']='Singh'
print(d1)
print(d1.popitem())
print(d1)
d1.clear()
print(d1)
del d1
#print(d1)
person={"name":"Rohit","age":20}

for key in person:
    print(key,end=" :")
    print(person[key])

