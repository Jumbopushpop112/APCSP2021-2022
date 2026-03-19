#import statement math
import math
#get the sides from the user
print("Right Triangle Time!")
print("Enter 3 integers")
side1 = int(input("Side 1:"))
side2 = int(input("Side 2:"))
side3 = int(input("Side 3:"))
#while looks that check to see if the user enters the sides the correctly 
while side2 < side1:
    print(str(side2) + " is smaller than " + str(side1) + " try again.")
    side2 = int(input("Enter Side 2 again:"))

while side3 < side2:
    print(str(side3) + " is smaller than " + str(side2) + " try again.")
    side3 = int(input("Enter Side 3 again:"))
#print the sides and check to see if it is a right triangle
print("The three sides you entered are: ",side1,side2,side3)
hyptonuse = math.sqrt(math.pow(side1,2) + math.pow(side2,2))
#print if it is a right triangle
if side3 == hyptonuse:
    print("These sides *do* make a right triangle. Yippy - Skippy!")
else:
    print("NO! These sides do not make a right triangle!") 
