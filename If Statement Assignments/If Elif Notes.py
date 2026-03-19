#get input from using and type cast to a float
grade = input("Enter in your grade please")
grade = int(grade)
#statements that check to see the grade 
if grade <= 59 and grade >= 0:
    print("Grade is an F")
elif grade <= 69 and grade >= 60:
    print("Grade is a D")
elif grade <= 79 and grade >= 70:
    print("Grade is a C")
elif grade <= 89 and grade >= 89:
    print("Grade is a B")
else:   
    print("Grade is an A") 

    
