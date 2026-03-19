file = open("dohmensdata.csv", "r")
fileData = file.readline()
print(fileData)
listFileData = fileData.split(",") 
for num in range(len(listFileData)):
    listFileData[num] = int(listFileData[num])
print(listFileData)
