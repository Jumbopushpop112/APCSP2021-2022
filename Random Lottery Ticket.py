import random
#main function
def main():
    listNum = []
    #create 6 random numbers and append them to a list. Check to see if it is not already in the list to avoid duplicates
    for x in range(0,5):
        randomNum = random.randint(1, 49)
        if randomNum not in listNum:
            listNum.append(randomNum)
    #print each number in the list
    for k in listNum:
        print(k)
main()