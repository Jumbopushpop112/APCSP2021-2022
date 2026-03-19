#dictionary that holds the values and the letters
scrabbleLetters = {
    "1": "A" "E" "I" "L" "N" "O" "R" "S" "T" "U",
    "2": "D" "G",
    "3": "B" "C" "M" "P",
    "4": "F" "H" "V" "W" "Y",
    "5": "K",
    "8": "J" "X",
    "10": "Q" "Z"
}
#user enters in a word
userWord = input("Enter a word for the Scramble Game. I will tell you how many points it is worth.")
sumWord = 0
#loop through the word
#capitalize each letter
#loop through the keys and the values
#if the letter is a value, set sum equal to key. After the loop print the number of points.
for letter in userWord:
    letter = letter.capitalize()
    for key, value in scrabbleLetters.items():
        #.items method returns a list of (key, value) tuples
        if letter in value:
           sumWord += int(key)
print("The word " + userWord + " is worth " + str(sumWord) + " points")