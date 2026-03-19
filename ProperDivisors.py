def getProperDivisors(someNum):
    listProperDivisors = []
    for i in range(1,someNum):
        if someNum % i == 0:
            listProperDivisors.append(i)
    return listProperDivisors
def validate(someNum):
    while True:
        try:
            someNum = int(someNum)
            return someNum
        except ValueError:
            someNum = input("Invalid number try again.")

def main():
    print("Enter a number. I'll show all of its proper divisors.")
    someNum = input("Enter a number:").strip()
    someNum = validate(someNum)
    listProperDivisors = getProperDivisors(someNum)
    print(listProperDivisors)
if __name__ == '__main__':
    main()