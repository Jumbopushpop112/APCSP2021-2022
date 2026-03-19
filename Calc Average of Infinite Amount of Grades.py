def getGrade():
    listGrades = []
    grade = input("Enter a grade. (blank to quit)")
    while grade != "":
        grade = validateGrade(grade)
        listGrades.append(grade)
        grade = input("Enter another grade. (blank to quit)")
    if len(listGrades) > 0:
        sumGrades = sum(listGrades)
        average = sumGrades/len(listGrades)
        averageGrade(average)
    else:
        print("you did not enter any grades.")
        print("program will now terminate! Better luck next time.")
        exit()
def averageGrade(average):
    if average >= 90 and average <= 100:
        print("Grade is an A!")
    elif average >= 80 and average <= 89:
        print("Grade is a B!")
    elif average >= 70 and average <= 80:
        print("Grade is a C!")
    elif average >= 60 and average <= 69:
        print("Grade is a D!")
    else:
        print("Grade is an F. You'll do great in law school!")

def validateGrade(grade):
     while True:
        try:
            grade = int(grade)
            return grade
        except ValueError:
            grade = input("Invalid grade, please try again.")
def main():
    getGrade()
main()
