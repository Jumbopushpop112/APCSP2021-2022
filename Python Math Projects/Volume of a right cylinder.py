'''

'''
import math
#variables that will be used for math
volCylinder = 0.0
radius = 0.0
height = 0.0
#user enters the radius and it is casted to a float
radius = input("Hey user, enter a radius")
radius = float(radius)
#user enters the height and it is casted to a float
height = input("Hey user, enter a height")      
height = float(height)   
#formula for cylinder volume
volCylinder = math.pi * (radius*radius) * height
#rounding the value to two decimal places
volCylinder = round(volCylinder, 2)
#display message 
print("Volume of a cylinder with a radius of " + str(radius) + " and a height of " + str(height) + " is " + str(volCylinder))
  


