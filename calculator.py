from math import *
from sys import *

"""
Make a program using functions that simulates a calculator and has the functions of addition, subtraction, multiplication, division, root, power
"""

def addition(number1, number2):
    result = number1 + number2
    return result

def subtraction(number1, number2):
    result = abs(number1 - number2)
    return result

def multiplication(number1, number2):

    result = number1 * number2
    return result

def division(number1, number2):

    result = number1 / number2
    return result

def square(number):

    result = number ** 2
    return result

def cube(number):

    result = number ** 3
    return result

def square_root(number):

    result = sqrt(number)
    return result

def cube_root(number):

    result = round(number ** (1/3))
    return result

def modulus(number1, number2):

    result = number1 % number2
    return result

print("----------")
print("CALCULATOR")
print("----------")

choice = int(input("Enter Your Choice:\n 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Square, \n6. Cube, 7. Square Root, 8. Cube Root, 9. Modulus, 10. Exit: "))

def main(choice):

    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 9:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
    elif choice == 5 or choice == 6 or choice == 7 or choice == 8:
        number = int(input("Enter a number: "))
    elif choice == 10:
        print("Thank you for using the CALCULATOR APP")
    else:
        print("Invalid choice.")

    if choice == 1:
        print("Addition of", number1, "and", number2, "is:", addition(number1, number2))

    elif choice == 2:
        print("Subtraction of", number1, "and", number2, "is:", subtraction(number1, number2))

    elif choice == 3:
        print("Product of", number1, "and", number2, "is:", multiplication(number1, number2))

    elif choice == 4:
        print("Division of", number1, "and", number2, "is:", division(number1, number2))

    elif choice == 5:
        print("Squared of", number, "is:", square(number))

    elif choice == 6:
        print("Cube of", number, "is:", cube(number))

    elif choice == 7:
        print("Square Root of", number, "is:", square_root(number))

    elif choice == 8:
        print("Cube Root of", number, "is:", cube_root(number))

    elif choice == 9:
        print("Modulus of", number1, "and", number2, "is:", modulus(number1, number2))

    elif choice == 10:
        exit()

    else:
        print("Please try again")

main(choice)
