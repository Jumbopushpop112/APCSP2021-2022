months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
    }
#months = {1: "January"}
#months = {"January" :1}
#accessing value of key via index notation
print(months["Apr"])
#accessing value of a key using a variable with index notation
abbrevMonth = "jan".capitalize()
try:
    print(months[abbrevMonth])
except KeyError:
    print("KeyError thrown, key not found")
    exit()
#Testing if key (abbreviated month) is in the dictionary. If so print
#its associated value
if abbrevMonth in months.keys():
    print(months[abbrevMonth])
else:
    print("key not found")
    exit()

#walking/iterating through a list and checking to see if each is a key
#in the dictionary
testString = "jan your mom feb"
listTestStr = testString.split()
for word in listTestStr:
    word = word.capitalize()
    if word in months.keys():
        print(months[word])
#Using typles as values in the dictionary
seasons = {"Spring":("Mar","Apr","May"),
           "Summer":("June", "July","Aug"),
           "Fall":("Sept", "Oct", "Nov"),
           "Winter":("Dec", "Jan", "Feb")}
month = "May"
#find the associated season for month
for key, value in seasons.items():
    #.items method returns a list of (key, value) tuples
    if month in value:
        print(key)#print the associated key to the value
#Walk/iterate through a string one letter at a time and print the weekday
#associated with it
weekdays = {"M":"Monday", "T":"Tuesday",
            "W":"Wednesday",
            "R":"Thursday",
            "F":"Friday"
            }
testString = "mtwrf".upper()
for letter in testString:
    print(weekdays[letter])