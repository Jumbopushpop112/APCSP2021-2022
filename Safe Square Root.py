#import statement
import math
#get number from user
print("SQUARE ROOT!")
number = int(input("Enter a number:"))
#while loop that executes when the user enters a number less than 0. It keeps prompting them until they do.
while number < 0:
    print("You can't take the square root of a negative number, silly.")
    number = int(input("Enter a number:"))
#take the square root of the number and then round it
squareRootNum = math.sqrt(number)
squareRootNum = round(squareRootNum,2)
#display the results of the number
print("The square root of " + str(number) + " is " + str(squareRootNum))