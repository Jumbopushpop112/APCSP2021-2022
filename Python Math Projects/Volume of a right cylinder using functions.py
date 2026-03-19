import math
def main():
    radius = int(input("Enter radius of the cylinder"))
    height = int(input("Enter height of the cylinder"))
    calcVolume_rightCylinder(radius, height)
def calcVolume_rightCylinder(radius, height):
    volume = int(math.pi * math.pow(radius, 2) * height)
    print(volume) 
main() 
