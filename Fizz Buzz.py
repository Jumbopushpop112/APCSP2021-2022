#print results using if statement checks. Return the output
def fizzBuzz(x):
    output = ""
    if x % 3 == 0 and x % 5 == 0:
        output += "FizzBuzz"
    elif x % 3 == 0:
        output += "Fizz"
    elif x % 5 == 0:
        output += "Buzz"
    else:
        output += str(x)
    return output
#generate random number and and send to function to check. return result
def main():
    for x in range(1,101):
        print(fizzBuzz(x))
main()
