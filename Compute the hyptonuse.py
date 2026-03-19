import math
import random
#function that does the math calculations and finds the hypotnuse of the triangle
def mathCalculations(side1, side2):
    hyptonuse = math.sqrt(math.pow(side1, 2) + math.pow(side2, 2))
    hyptonuse = round(hyptonuse, 2)
    print(side1)
    print(side2)
    print(hyptonuse)

#main function that generates the two sides
def main():
    side1 = random.randint(1, 10)
    side2 = random.randint(1, 10)
    mathCalculations(side1,side2)
main()
