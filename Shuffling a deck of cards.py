import random
#shuffle the deck using the swap algorithm
def shuffleDeck(myDeck):
   for randNum1 in range(len(myDeck)):
       randNum2 = random.randint(0, len(myDeck)-1)
       Temp = myDeck[randNum1]
       myDeck[randNum1] = myDeck[randNum2]
       myDeck[randNum2] = Temp
   return myDeck
#print table 4 rows of 13
def printTable(myDeck):
    temp = myDeck
    for x in range(4):
        for y in range(13):
            print(temp[x * 13 + y], end=" ")
        print()
#fill the deck at room time
def fillDeck():
    cardVal = ""
    listSuits = ["s", "d", "h", "c"]
    listDeck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
    myDeck = []
    for suit in listSuits:
        for num in listDeck:
            myDeck.append(num + suit)
    return myDeck
#main function that prints the og deck and the shuffled deck. Functions are called to fill the deck
def main():
    myDeck = fillDeck()
    print("Original Deck:")
    printTable(myDeck)
    print("Shuffled Deck:")
    printTable(shuffleDeck(myDeck))
main()
