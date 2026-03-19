import random
#check to get the ordinal value by doing modulus division
def findNum(num):
    if num % 10 == 1 and num != 11:
        return str(num) + "st"
    elif num % 10 == 2:
        return str(num) + "nd"
    elif num % 10 == 3:
        return str(num) + "rd"
    else:
        return str(num) + "th"
#get number, call function and print the results.
def main():
    num = int(input("Enter a number between 1 and 100."))
    findNum(num)
    print(findNum(num))
main()