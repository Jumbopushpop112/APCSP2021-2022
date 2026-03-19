'''
Write a program that calculates the volume of a sphere.
volSphere = 4/3 * pi * radius cubed
Boss man said to get radius from the user
'''
import math 
volSphere = 0.0
radius = 0.0

#get radius from the user and store in variable 'radius'
radius = input("Hey user enter a stinking radius: ")
#convert radius to a float
radius = float(radius)
volSphere = 4/3 * math.pi * (radius*radius*radius)
volSphere = str(volSphere) 
print("Volume of sphere is: " + volSphere) 
