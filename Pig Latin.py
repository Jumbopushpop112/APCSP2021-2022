def convertWord(word):
    listVowels = ["a","e","i","o","u"]
    #think becomes inkthay
    #access each letter at a time in word
    if word[0:1].lower() in listVowels:
        return word + "way "
    for letter in word:
        if letter.lower() in listVowels:
            posVowel = word.index(letter)
            #extract all letters up to posVowel
            beginWord = word[0:posVowel]
            convertedWord = word[posVowel:] + beginWord + "ay "
            return convertedWord
def translateSentence(theSentence):
    listWords = theSentence.split()
    resultString = ""
    for word in listWords:
        resultString = resultString + convertWord(word)
    return resultString

def main():
    #print(convertWord("Office"))
    sent = "Your mama don't dance and your daddy don't rock and roll"
    convertedSentence = translateSentence(sent)
    print(convertedSentence)
main()