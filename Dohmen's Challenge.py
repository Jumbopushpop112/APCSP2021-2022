def flipList(mainList):
    for itemList in mainList:
        itemList.reverse()
        print(itemList)
def main():
    mainList = [[1, 22, 31, 47, 5], [6, 7, 83, 9, 10], [11, 12, 13, 14, 15], [16, 17, 188, 19, 207]]
    flipList(mainList)
main()


