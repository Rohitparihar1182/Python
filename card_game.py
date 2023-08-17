import random
import my_deck
deck=my_deck.Deck()
def add(L):
    n1=[]
    n2=[]
    maxn=len(L)
    for i in range(3):
        
        num=random.randint(0,maxn)
        x=L[num]
        n1.append(x)
        del L[num]
        maxn-=1
        num=random.randint(0,maxn)
        x=L[num]
        n2.append(x)
        del L[num]
        maxn-=1
    return n1,n2
c1,c2=add(deck)
p1 = input("Player 1 Name :- ")
p2 = input("Player 2 Name :- ")
print(p1," cards:",c1)
print(p2," cards:",c2)

