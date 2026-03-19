
import random
#create the deck and append each item to the list
def createDeck():
    listSuits = ["s","d","h","c"]
    listDeck = ["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
    myDeck = []
    for suit in listSuits:
        for num in listDeck:
            myDeck.append(suit + num)
    return myDeck

#shuffle deck and pop a value out of the list randomly and add it to the new list
def shuffleDeck(myDeck):
    shuffleDeck = []
    while len(myDeck) > 0:
        shuffleDeck.append(myDeck.pop(random.randint(0,len(myDeck)-1)))
    return shuffleDeck
#main function that prints the original deck and the deck shuffled
def main():
    myDeck = createDeck()
    print("Original Deck created:\n"+str(myDeck))
    print("Original Deck shuffled:\n"+str(shuffleDeck(myDeck)))