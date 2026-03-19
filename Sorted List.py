def main():
    listNum = []
    num = input("Enter a number!")
    #while loop that repeats until the user enters a blank string
    while num != "":
        listNum.append(num)
        num = input("Enter a number!")
    #make a copy of the list and sort it
    listNumCopy = listNum[:]
    listNumCopy.sort()
    #print the lists and print false if they aren't sorted and print true if they are sorted
    print("Original list ",listNum)
    print("Copy of list sorted",listNumCopy)
    print(isSorted(listNum, listNumCopy))
#check to see if the list is sorted
def isSorted(listNum, listNumCopy):
    if listNum == listNumCopy:
        return True
    else:
        return False
main()