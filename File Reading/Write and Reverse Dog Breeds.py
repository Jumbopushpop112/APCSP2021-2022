import random

def writeToFile(fileName, listDogBreeds):
    try:
        userFile = open(fileName, "w")
        userFile.write(listDogBreeds[0])
        for i in range(len(listDogBreeds)-1):
            userFile.write("," + listDogBreeds[i+1])
        userFile.close()
        userFile = open("dogBreedsReversed.csv", "r")
        userFileLine = userFile.readline()
        userFileList = userFileLine.split(",")
        print("List written to file:",userFileList)
        userFileList.reverse()
        print("List written to file but reversed:",userFileList) 
    except IOError:
        print("Can't find file " + fileName)
def main():
    listDogBreeds = ["Poodle", "Retriever", "Labrador", "Chihuahua", "Bulldog"]
    writeToFile("dogBreedsReversed.csv", listDogBreeds)
main()
