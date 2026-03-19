import random
def gameTime():
    tries = 1
    sports = ["Baseball","Basketball","Football","Soccer","Cricket","Croquet","Tennis"]
    randomWord = random.choice(sports)
    print("Alright, so here is how the game works. I have a list of sports and a random word is selected each time\n")
    print("The list consists of 7 choices and one of them is the correct word!")
    print(randomWord)
    wordGuess = input("Enter the sport you think the random word is!")
    while wordGuess != randomWord:
        tries += 1
        wordGuess = input("Sorry! That isn't the sport word. Try again!")
    if wordGuess == randomWord:
        if tries == 1:
            print("You are a good guesser. It looks like you guessed the right word in " + str(tries) + " try. Nice job!")
        else:
            print("You are a good guesser. It looks like you guessed the right word in " + str(tries) + " tries. Nice job!")

gameTime()