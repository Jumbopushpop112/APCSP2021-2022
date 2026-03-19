#AP CSP Create Task Code
def getStoryOfNumber(x):
    if x == 1:
        x = "1 - Pythagoreans did not consider 1 to be a number at all because number means plurality and 1 is singular."
    elif x == 2:
        x = "2 - The number 2 symbolizes basic dualities such as: me/you, dead/alive and so on! Pretty cool am I right?"
    elif x == 3:
        x = "3 - 3 is used in a lot of fairy tales such as The Three Wishes, The Three Little Pigs and The Three Billy Goats Gruff!"
    elif x == 4:
        x = "4 - The number 4 represents the 4 elements of: Earth, Wind, Fire and Water. It also represents the four directions on a compass as well!"
    elif x == 5:
        x = "5 - The first even and odd numbers add to 5 which is this number."
    elif x == 6:
        x = "6 - 6 is the sum and the production of the first three numbers (1,2,3)"
    elif x == 7:
        x = "7 - 7 is considered a lucky number by many. Perhaps this means you will get lucky?"
    elif x == 8:
        x = "8 - The Square any odd number, subtract one and the number 8 will always be a multiple of the value, which is this value."
    elif x == 9:
        x = "9 - The number 9 represents pain and sadness to many."
    elif x == 10:
        x = "10 - This number represents perfection or completeness."
    else:
        x = "This number is too big for me. I can't get a fact!"
    return x
def displayList(displayLength,listNums):
    print("Your list with the facts!")
    if displayLength == "N":
        for x in listNums:
            print(getStoryOfNumber(x))
    if displayLength == "Y":
        for x in listNums:
            print(getStoryOfNumber(x))
        if len(listNums) >= 1 and len(listNums) <= 3:
            print("With a length of " + str(len(listNums)) + " your list has a small size!")
        if len(listNums) > 3 and len(listNums) < 6:
            print("With a length of " + str(len(listNums)) + " your list has a medium size!")
        if len(listNums) >= 6 and len(listNums) <= 10:
            print("With a length of " + str(len(listNums)) + " your list has a large size!")
    print("Thanks for using this program. Hope you enjoyed learning these facts about the numbers!")
def main():
    listNums = []
    numChoice = int(input("Enter a number 1-10 here to add to a list. Once you are done, I will replace the number in the list with the fact about it! (0 to quit):"))
    while numChoice != 0:
        listNums.append(numChoice)
        numChoice = int(input("Enter your number here to add to a list (0 to quit):"))
    displayLength = input("Would you like to tell me what size of list you have according to my knowledge? Y/N:")
    if displayLength == "Y":
        displayList("Y", listNums)
    else:
        displayList("N", listNums)
main()

