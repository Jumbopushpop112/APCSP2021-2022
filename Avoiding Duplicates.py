def main():
    #main function, array and input
    listWords = []
    word = input("Enter a word!")
    #repeat until the user enters a blank string
    while word != "":
        #if the word isn't in the list append, it
        if word not in listWords:
            listWords.append(word)   
        word = input("Enter a word!")
    #print each word
    for x in listWords:
        print(x) 
main()
