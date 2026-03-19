#import library to find statistics
import statistics
import random
#fucntion that sorts the value and uses .median to find the median
def sortValues(numList):
    numList.sort()
    print(numList)
    print(statistics.median(numList))
#main function with input for numbers that puts them in a list and the sends them to the function
def main():
    num1 = random.randint(1,10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    numList = [num1, num2, num3]
    sortValues(numList)
main()