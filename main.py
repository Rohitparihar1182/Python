import module

option = module.input_option()


if option == 1:
    numbers = module.input_numbers()
    print(module.add(numbers[0], numbers[1]))
elif option == 2:
    numbers = module.input_numbers()
    print(module.substract(numbers[0], numbers[1]))
elif option == 3:
    numbers = module.input_numbers()
    print(module.mutliply(numbers[0], numbers[1]))
elif option == 4:
    numbers = module.input_numbers()
    print(module.divide(numbers[0], numbers[1]))
else:
    print("invalid input please try again")
