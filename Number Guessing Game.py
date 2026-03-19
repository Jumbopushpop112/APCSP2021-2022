#variables and import statement
import random
num = str(random.randint(1,100))
print("I'm thinking of a number between 1-100.  You have 7 guesses.")
guess = input("First guess")
tries = 1
#while loop that checks to see if the number is too low or too high
while guess != num and tries < 7:
    if guess < num and guess.isnumeric():
        print("Sorry, you are too low.")
    if guess > num and guess.isnumeric():
        print("Sorry, that guess is too high.")
    tries +=1
    guess = input("Guess #" + str(tries) + ":")
#if statement if the users number entered is equal to the random generated. Else, print they lost
if guess == num:
    print("You guessed it!  What are the odds?!?")
else:
    print("Sorry, you didn't guess it in 7 tries.  You lose.")

