print("Welcome to Gaji's Calculator")
name = input("What is your name? ")
print(f"Hello {name}")

first_number = int(input("Input the first number: "))
second_number = int(input("Input the second number:\n"))


def operation():
    print(f"These are the values you provided:\n First Number: {first_number}\n Second Number: {second_number}\n")
    print(
        "What kind of operation do you want to perform to the values provided?\n Addition(press 1)\n Subtraction(press 2)\n Multiplication(press 3)\n Division(press 4)\n")
    value = int(input("Value? "))
    if value == 1:
        result = first_number + second_number
        print(f"This is the Result: {result}")

    elif value == 2:
        result = first_number - second_number
        print(f"This is the Result: {result}")

    elif value == 3:
        result = first_number * second_number
        print(f"This is the Result: {result}")

    elif value == 4:
        result = first_number / second_number
        print(f"This is the Result: {result}")

    else:
        print("Invalid value, ensure your value is an INTEGER")
        operation()


operation()