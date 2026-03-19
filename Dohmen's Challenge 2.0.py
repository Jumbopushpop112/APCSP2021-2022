def printDiagonal(mainList):
    newList = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for x in range(len(mainList)):
        for y in range(len(newList[x])):
            newList[y][x] = mainList[x][y]
    for item in newList:
        print(item)
def main():
    mainList = [[1, 22, 31, 47, 5], [6, 7, 83, 9, 10], [11, 12, 13, 14, 15], [16, 17, 188, 19, 207]]
    printDiagonal(mainList)
main()