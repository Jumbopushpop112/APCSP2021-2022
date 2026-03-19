#write a function that receives a decimal number 0-1023 and converts it to binary
def convertToBinary(userNum):
    listNums = [512,256,128,64,32,16,8,4,2,1]
    i = 0
    binaryDigit = ""
    while i<len(listNums):
        if userNum >= listNums[i]:
            userNum -= listNums[i]
            binaryDigit += "1"
        else:
            binaryDigit += "0"
        i += 1
    print(binaryDigit)
def main():
    userNum = int(input("Enter a number between 0-1023 and I will convert it to binary"))
    convertToBinary(userNum)
main()