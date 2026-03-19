from ProperDivisors import getProperDivisors

listPerfectNumbers = []  # holds proper nums between 1-10,000
def isPerfect(someNum):
    '''
    get the list of proper divisors for someNum
    add the values in the returned list
    if the sum is equal to someNum return true, else return false
    '''
    listNum = getProperDivisors(someNum)
    sumNums = sum(listNum)
    if sumNums == someNum:
        return True
    else:
        return False
def main():
    for i in range(1, 10001):
        if isPerfect(i):
            listPerfectNumbers.append(i)
    print(listPerfectNumbers)
if __name__ == '__main__':
    main()