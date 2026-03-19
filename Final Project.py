import turtle
import random
listNums = []
listValues = []
bob = turtle.Turtle()
bob.speed(30)
def drawAxis():
    bob.left(90)
    bob.forward(500)
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    bob.right(90)
    bob.forward(500)
def drawBars(height,num,color):
    height = height * 10
    bob.fillcolor(color)
    bob.begin_fill()
    
    bob.forward(height)  
    bob.right(90)
    bob.forward(20)
    bob.write(num,)
    bob.forward(20)
    bob.right(90)
    bob.forward(height)
    bob.end_fill()
def repositionTurtle(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.setheading(90)
def main():
    oneAndTwenty = 0
    twentyOneFourty = 0
    fourtyOneSixty = 0
    sixtyOneToEighty = 0
    eightOneToHundred = 0
    window = turtle.Screen()
    #generate list of random nums
    for x in range(200):
        randomNum = random.randint(1,100)
        if randomNum >=1 and randomNum <=20:
            oneAndTwenty += 1
        if randomNum >= 21 and randomNum <= 40:
            twentyOneFourty += 1
        if  randomNum >= 41 and randomNum <= 60:
            fourtyOneSixty += 1
        if randomNum >= 61 and randomNum <= 80:
            sixtyOneToEighty += 1
        if randomNum >= 81 and randomNum <= 100:
            eightOneToHundred += 1
    tupleColors = ("#0320fc", "#0bfc03", "#50C7B5", "#C7C550", "#5065C7", "#eb34e5", "#3493eb", "#34eb99", "#eb3434", "#ebba34", "#a834eb", "#eb3462")
    listNums.append(randomNum)
    listValues.append(oneAndTwenty)
    listValues.append(twentyOneFourty)
    listValues.append(fourtyOneSixty)
    listValues.append(sixtyOneToEighty)
    listValues.append(eightOneToHundred)
    drawAxis()
    repositionTurtle(0,0)
    startX = 0
    startY = 0
    bob.goto(20,0)    
    for x in range(5):
        color = random.choice(tupleColors)
        startX = bob.xcor() + 100
        drawBars(listValues[x],listValues[x],color)
        repositionTurtle(startX,startY)
    window.exitonclick()
main()
