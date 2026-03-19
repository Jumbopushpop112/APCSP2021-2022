import random
def playGame():
    opponentChoices = ["Rock", "Paper", "Scissors"]
    opponentChoice = random.choice(opponentChoices)
    numWins = 0
    for x in range(1,6):
        print("Game:" + str(x))
        userChoice = input("Enter Rock, Paper or Scissors")
        if userChoice == opponentChoice:
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("You tied!")
        if userChoice == "Rock" and opponentChoice == "Paper":
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("Opponent wins!")
        if userChoice == "Rock" and opponentChoice == "Scissors":
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("You win!")
            numWins += 1
        if userChoice == "Paper" and opponentChoice == "Rock":
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("You win!")
            numWins += 1
        if userChoice == "Paper" and opponentChoice == "Scissors":
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("Opponent wins!")
        if userChoice == "Scissors" and opponentChoice == "Paper":
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("You win!")
            numWins += 1
        if userChoice == "Scissors" and opponentChoice == "Rock":
            print("You chose " + userChoice)
            print("Computer chose " + opponentChoice)
            print("You lost!")
    print("You won " + str(numWins) + " times out of 5 times.")
def main():
    playGame()
main()
