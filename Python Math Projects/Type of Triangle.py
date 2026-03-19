side1 = int(input("Enter first side of triangle"))
side2 = int(input("Enter second side of traingle"))
side3 = int(input("Enter third side of triangle"))
if(side1 == side2 and side1 == side3):
    print("Equilateral traingle") 
elif(side1 == side2 or side1 == side3 or side2 == side3):
    print("Isosceles triangle") 
else:      
    print("Scalene triangle")        
