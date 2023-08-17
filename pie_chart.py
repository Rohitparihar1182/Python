import matplotlib as plt
Players="Sachin Tendulkar","Sunil Gavaskar","MS Dhoni"
score=[40,35,30,10]
explode=(0.1,0,0,0)

fix1,ax1=plt.subplots()
ax1.pie(score,explode=explode,labels=Players,autopct='%1.1f%%',shodow=True,startangle=90)
ax1.axis('equal')
plt.show()
