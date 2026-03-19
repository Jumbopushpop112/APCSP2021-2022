#import modules and set up the turtle
import turtle
import time
square = turtle.Turtle()
square.shape("turtle")
square.hideturtle()
#draw the squares for all three functions
def drawSquares(center, sideLength):
    square.penup()
    square.speed(10)
    square.goto(center - sideLength/2, 0 + sideLength/2)
    square.pendown()
    for x in range(1, 5):
        square.forward(sideLength)
        square.right(90)
#draw first pattern
def firstPattern():
    turtle.Screen().bgcolor("light green")
    for x in range(1, 6):
        square.width(3)
        square.pencolor("deep pink")
        drawSquares(-150 + 50 * x,20)
#draw second pattern
def secondPattern():
    time.sleep(2)
    square.reset()
    turtle.Screen().bgcolor("light green")
    square.hideturtle()
    for x in range(1, 6):
        square.width(3)
        square.pencolor("red")
        drawSquares(0, 70 - 10 * x)
#draw third pattern
def thirdPattern():
    time.sleep(2)
    square.reset()
    turtle.Screen().bgcolor("white")
    square.hideturtle()
    for x in range(1,20):
        square.width(2)
        square.pencolor("green")
        drawSquares(0, 212 - 10 * x)
firstPattern()
secondPattern()
thirdPattern()
