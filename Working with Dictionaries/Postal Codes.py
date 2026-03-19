#dictionary with the postal codes
postalCodes = {
    "Newfoundland": "A",
    "Nova Scotia": "B",
    "Prince Edward Island": "C",
    "New Brunswick": "E",
    "Quebec": "G" "H" "J",
    "Ontario": "K" "L" "M" "N" "P",
    "Manitoba": "R",
    "Saskatchewan": "S",
    "Alberta": "T",
    "British Columbia": "V",
    "Nunavut": "X",
    "Northwest Territories": "X",
    "Yukon": "Y"
}
userPostalCode = input("Enter a postal code:")
#get first and second characters and match up accordingly
firstChar = userPostalCode[0:1]
secondChar = userPostalCode[1:2]
addressType = ""
if secondChar == "0":
    addressType = "rural"
    for key, value in postalCodes.items():
        if firstChar in value:
            print("Postal code is for a " + addressType + " address in " + key)
else:
    addressType = "urban"
    for key, value in postalCodes.items():
        if firstChar in value:
            print("Postal code is for a " + addressType + " address in " + key)
