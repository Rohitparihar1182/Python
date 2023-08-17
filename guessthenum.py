import random
maxn=10
n=random.randint(1,maxn)
print("welcome to guess the number game!")
guess=None
while guess!=n:
    guess=int(input("try"))
    if guess>n:
        print("high")
    elif guess<n:
        print("low")

print("Congratulations! you won")
