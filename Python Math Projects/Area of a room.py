area = 0.0;
#get input from  the user and type cast both to a float
length = input("Enter the length of the room in feet")
length = float(length)
width = input("Enter the width of the room in feet")
width = float(width)
#math is done to get the area
area = length * width 
#combining strings and printing the area 
print("Area of a room with a length of " + str(length) + " feet and a width of " + str(width) + " feet is " + str(area) + " feet")
 
