#imports
import time

#user startup
username = input("What is your name? ")
print("Welcome, " + username, ". It is time to play hangman!")
print("")

#wait
time.sleep(1)
print("Ready to start guessing...?")
time.sleep(0.5)

#this is where the word is set
word = "nationalism"


#setting variable to handle guesses
guesses = ""

#setting variable to handle remaining turns
turns = 10

#while loop to handle the action
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,)
        else:
            print("_",)
            failed += 1
    if failed == 0:
        print("You won!")
        break
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong guess.")
        print("You have " + str(turns) + " more guesses!")
        if turns == 0:
              print ("You loose!")
        time.sleep(2)
