area = 0.0
import math
length = input("Enter the length of your field in feet")
length = float(length)
width = input("Enter the width of your field in feet")
width = float(width)
area = length * width  
acres = area / 43560 
acres = round(acres, 2)            
print("The area of your field is " + str(area) + " and your land has " + str(acres) + " acres in it")  


