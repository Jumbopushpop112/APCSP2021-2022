import random
#generate random number 1-10
number = random.randint(1, 10)
print("I have randomly created a number between 1 and 10. Try to guess it. Enter a number please")
#get number and cast to an int
userGuess = int(input("Your guess:"))
guesses = 1
#while loop that repeats the input if the user's guess is equal to the random number.
while userGuess != number:
    print("That is incorrect. Guess again")
    guesses += 1
    userGuess = int(input("Your guess:"))
print("That's right.")
#print the amount of guesses it took
print("It took you " + str(guesses) + " guesses to guess the number!")

