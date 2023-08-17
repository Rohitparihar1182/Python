from tkinter import *
root=Tk()
root.geometry("800x800")
root.title('''The Times Of India  28/02/2021''')
topic=Label(root,text="COVID-19: global vaccine promises ring hollow",font=("baskerville",20,"bold")).pack(anchor="w",side=TOP)
matter=Label(root,text="Almost 130 countries are yet to receive a single COVID-19 vaccine dose, \n as ten high-income countries secure the majority",font=("baskerville",15)).pack(anchor="w")
news=Label(root,text='''This week, the first COVID-19 vaccine doses from the United Nations-led COVAX
initiative arrived in Africa. This is a long-awaited piece of good news in a climate
where vaccine procurement for developing countries has been hampered by empty
promises,delays, infrastructure challenges and prejudice.''',font=("baskerville",14)).pack(anchor="w")


root.mainloop()
