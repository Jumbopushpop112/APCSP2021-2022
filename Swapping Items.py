import random
deck = []
listSuits = ["s", "h", "c", "d"]
listValues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
for suit in listSuits:
    for num in listValues:
        deck.append(suit + num)
randNum1 = random.randint(0, 12)
randNum2 = random.randint(0, 12)
Temp = deck[randNum1]
deck[randNum1] = deck[randNum2]
deck[randNum1] = Temp
print(Temp)
