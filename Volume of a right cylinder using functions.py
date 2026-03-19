import math
#main function that gets the radius and the height
def main():
    radius = float(input("Enter radius of the cylinder"))
    height = float(input("Enter height of the cylinder"))
    calcVolume_rightCylinder(radius, height)
#function that does the math and prints it
def calcVolume_rightCylinder(radius, height):
    volume = float(math.pi * math.pow(radius, 2) * height)
    volume = round(volume, 2)
    print("Height entered is: " + str(height))
    print("Radius entered is: " + str(radius))
    print("Volume is " + str(volume))
main()
