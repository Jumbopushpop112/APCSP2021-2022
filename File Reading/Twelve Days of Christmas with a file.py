#list of all gifts
listGifts = []
fileName = open("Christmas.csv")
for line in fileName.readlines():
    line = line.strip("\n")
    listGifts.append(line)
#get ordinal verse values
def getOrdinal(num):
    ordinals = ["?","First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelth"]
    return ordinals[num]
#get verse number
def getVerse(num):
    verse = getFirstTwoLines(num)
    for k in range(num, 0, -1):
        if num == 1:
            verse = verse + listGifts[0] + "\n"
        else:
            verse = verse + listGifts[k]+ "\n"
    return verse
#print lines
def getFirstTwoLines(num):
    print("On the " + getOrdinal(num) + " day of Christmas\nMy true love sent to me")
    for k in range(num):
         num-=1
         print(listGifts[num])
#enter verse number
def main():
    print("On the " + getOrdinal(1) + " day of Christmas\nMy true love sent to me\nA partridge in a pear tree\n")
    for verse in range(2,13):
        getFirstTwoLines(verse)
        print("")
main()