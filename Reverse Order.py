#main function
def main():
    #list
    listNum = []
    num = input("Enter a number! 0 to quit")
    #while loop that keeps repeating until the user enters a 0
    while num != "0":
        listNum.append(num)
        num = input("Enter a number! 0 to quit")
    #reverse the list
    listNum.reverse()
    #print out each element
    for x in listNum:
        print(x)
main()