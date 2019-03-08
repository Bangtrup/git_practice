#variables
number1 = 0
number2 = 0


#functions
def compare(number1, number2):
    if number1 < number2:
        print(number2 + " is the larger number!")
    if number1 > number2:
        print(number1 + " is the larger number!")

print("This is my first Python application. This script will compare two numbers, and state the largest of them.")

print("Input the first number - press ENTER when you're done.")
number1 = input()

print("Input the second number - press ENTER when you're done.")
number2 = input()

compare(number1, number2)
