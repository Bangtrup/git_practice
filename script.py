#imports




#variables
number1 = 0
number2 = 0


#functions
def compare(number1, number2):
    if number1 < number2:
        print(number2 + " is the larger number!")
    if number1 > number2:
        print(number1 + " is the larger number!")

#software
print("This is a collection of basic Python functions, which I have tried to program myself.")
print("The intention is to program a fully written assitant for the co-op game, Keep talking and nobody explodes.")
print("")
print("Currently the functions are as listed, pick the number and press ENTER and the function will launch.")
print("")
print("1: Number comparator")
print("2: String length counter")
print("3: Odd or even numbers")
print("4: Whatever will be developed in the future")

selection = input()

#Number Comparator
if selection == "1":
    print("Please enter first comparator:")
    number1 = input()
    print("Please enter second comparator:")
    number2 = input()
    compare(number1, number2)

#String length counter
if selection == "2":
    print("Please write the phrase, of which you'd like to know the length.")
    string = input()
    string_length = len(string)
    print("The written string is " + str(string_length) + " characters long.")
    
