"""
PEMDAS
Parentheses
Exponents
Multiplication
Division
Addition
Subtraction
Method for solving an equation
"""
#floor division which returns a decimal and rounds it down
problem1 = 7 //6
print(problem1)
#modulus division which returns the remainder
problem2 = 8%5 #will return 3 
print(problem2)
problem3 = 1/4 % 5 #will always return 0.25 or the fraction as a decimal 
print(problem3)
problem4 = 1/4 * 3 + 6%5 #work from left to right in a problem like this. Answer is 1.75 
print(problem4)
#first part is using math.floor. However, it equals 0 so the answer is 5 
problem5 = 1/4 // 3  + 5
print(problem5)
#first side is 0 *1 + 6, which is equal to 6
problem6 = 4%2 * 5//4 + 6 
print(problem6)
#another floor division problem  
problem7 = 5//4    
print(problem7)
#simple arithmetic problem  
problem8 = 5%4 * 5 + 7%4 
print(problem8)
#another simple math problem
problem9 = 1/4 * 3 + 7//8     
print(problem9)
#when you have math problems with % and * work from left to right.  
problem10 = 6*7%5+4/4 
print(problem10)
#another math problem
problem11 = 1/4*3+5*9        
print(problem11) 
#math.floor practice. When the number on the left is smaller than the number on the right it will always be 0
problem12 = 6//7      
print(problem12)
x = 16 - 2 * 5//3 + 1
print(x)  
 
 
