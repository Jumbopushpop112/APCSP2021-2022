import random
#check the string value integer and print the english word
def findString(number):
    print(number)
    if number == 1:
        print("First")
    elif number == 2:
        print("Second")
    elif number == 3:
        print("Third")
    elif number == 4:
        print("Fourth")
    elif number == 5:
        print("Fifth")
    elif number == 6:
        print("Sixth")
    elif number == 7:
        print("Seventh")
    elif number == 8:
        print("Eighth")
    elif number == 9:
        print("Ninth")
    elif number == 10:
        print("Tenth")
    elif number == 11:
        print("Eleventh")
    elif number == 12:
        print("Twelfth")
    else:
        print("")
#main function that generates a random number
def main():
    number = random.randint(1, 12)
    findString(number)
main()