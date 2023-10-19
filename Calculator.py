def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("1. Enter '1' for addition")
    print("2. Enter '2' for subtraction")
    print("3. Enter '3' for multiplication")
    print("4. Enter '4' for division")
    print("5. Enter '0' to end the program")

    user_input = input(": ")

    if user_input == "exit":
        break
    elif user_input == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", add(num1, num2))
    elif user_input == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", subtract(num1, num2))
    elif user_input == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", multiply(num1, num2))
    elif user_input == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", divide(num1, num2))
    elif user_input == "0":
        print("The Calculator is closed Thank You")
    else:
        print("Invalid input")
