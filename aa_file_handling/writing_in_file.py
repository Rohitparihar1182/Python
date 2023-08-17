f = open('another.txt', 'w')
f.write('''Hi,I am rohit
parihar
i live in bahuli''')

f.close()
f=open('another.txt','r')
a=f.read()
print(a.find('rohit'))
f.close()
