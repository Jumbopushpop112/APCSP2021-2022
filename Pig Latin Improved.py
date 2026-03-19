def convertWord(word):
    lastChar = (word[len(word) - 1:-2:-1])
    convertedWord = ""
    listVowels = ["a","e","i","o","u"]
    listPunctuation = ["!",".",",","?"]
    havePunct = False
    #think becomes inkthay
    #access each letter at a time in word
    if lastChar in listPunctuation:
        havePunct = True
        word = word[0:len(word)-1]
    if word[0:1].lower() in listVowels:
        convertedWord = word + "way"
    for letter in word:
        if letter.lower() in listVowels:
            posVowel = word.index(letter)
            #extract all letters up to posVowel
            beginWord = word[0:posVowel]
            convertedWord = word[posVowel:] + beginWord + "ay"
            break
    if havePunct == True:
        convertedWord = convertedWord + lastChar
    else:
        converetedWord = convertedWord + " "
    if word[0:1].isupper():
        convertedWord = convertedWord.capitalize()
    return convertedWord
def translateSentence(theSentence):
    listWords = theSentence.split()
    resultString = ""
    for word in listWords:
        resultString = resultString + convertWord(word)
    return resultString
def main():
      print(convertWord("Science!")) 
      print(convertWord("Computer"))
main()




