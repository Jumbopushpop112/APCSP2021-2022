#function that starts the game and empties the piles and keeps on going until the the piles are empty.
def gameTime(numA, numB, numC):
    while numA > 0 or numB > 0 or numC > 0:
        print("A:" + str(numA) + " B:" + str(numB) + " C:" + str(numC))
        pileChoice = input("Choose a pile")
        removingAmount = int(input("How many to remove from pile " + pileChoice + ":"))
        if pileChoice == "A":
            numA = numA - removingAmount
        if pileChoice == "B":
            numB = numB - removingAmount
        if pileChoice == "C":
            numC = numC - removingAmount
    #after the loop is over (the piles are empty) then it prints the numbers in the piles and prints out the message saying the game is over.
    print("A:" + str(numA) + " B:" + str(numB) + " C:" + str(numC))       
    print("All piles are empty. Nice work!")  
#main function           
def main():
    numA = 3
    numB = 3 
    numC = 3
    gameTime(numA, numB, numC)
main()
