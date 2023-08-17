def input_option():
    choice = int(input(
       ''' 1 to add
2 to substract
3 to multiplication
4 to divide

enter: '''
    ))
    return choice


def input_numbers():
    numbers = input("enter the numbers: ").split(" ")
    temp = []

    for number in numbers:
        temp.append(int(number))
    return temp


def substract(a, b):
    return a - b


def mutliply(a, b):
    return a * b


def add(a, b):
    return a + b


def divide(a, b):
    if a < b:
        return b/a
    else:
        return a/b

