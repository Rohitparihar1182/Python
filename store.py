class store:
    def prices(self):
        self.my_dict={}
        self.my_dict[101]=100
        self.my_dict[102]=200
        self.my_dict[103]=150
        self.my_dict[104]=300
        self.my_dict[105]=900
    def define(self):
        print("list of products are:-")
        for key in self.my_dict:
            print("item ",key,"cost=Rs",self.my_dict[key])
        total=0
        z=None
        while z!="stop":
            print("enter id of product you want")
            x=int(input())
            if x in self.my_dict:
                
                y=int(input("enter quantity"))
                z=input("enter'stop'to stop shopping")
                total+=y*(self.my_dict[x])
            else:
                print("item ",x,"is not available")
        print("your total is=",total)
s=store()
s.prices()
s.define()

