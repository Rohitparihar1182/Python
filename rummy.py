import my_deck
import random
def two_players(deck):
    p1=[]
    p2=[]
    maxn=51
    for i in range(11):
        x=random.randint(0,maxn)
        
        p1.append(deck[x])
        deck.pop(x)
        maxn-=1
        y=random.randint(0,maxn)
        p2.append(deck[y])
        deck.pop(y)
        maxn-=1
    print("player 1 cards:",p1)
    print("player 2 cards:",p2)
print("Welcome to Rummy circle :")

d=my_deck.Deck()
two_players(d)
