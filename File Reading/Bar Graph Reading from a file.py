import turtle
#drawing the bars
def makeRectangle(myTurtle, height, width, color):
    #precondition is that the turtle is facing north
    #set up fillcolor
    myTurtle.fillcolor(color)
    myTurtle.begin_fill()
    myTurtle.forward(height)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)
    myTurtle.end_fill()
#reposition the turtle after drawing
def repositionTurtle(myTurtle, newX, newY, newHeading):
    #headings are: 0 =east, 90=north, 180=west, 270=south
    myTurtle.penup()
    myTurtle.goto(newX, newY)
    myTurtle.pendown()
    myTurtle.setheading(newHeading)
#draw the bars
def labelBars(myTurtle, listXCoord, listYCoord, tupMonths):
    for i in range(len(listXCoord)):
        repositionTurtle(myTurtle, listXCoord[i]-20, listYCoord[i]-20, 0)
        myTurtle.write(tupMonths[i], align="center")
#draw x-axis
def drawX(myTurtle, forwardMeter):
    myTurtle.forward(forwardMeter)
#draw y axis
def drawY(myTurtle, turnMeter, backMeter, forwardMeter):
    myTurtle.right(turnMeter)
    myTurtle.back(backMeter)
    myTurtle.forward(forwardMeter)
#draw the title bars on the y axis
def drawYAxTitles(myTurtle):
    distanceLength = 30
    for i in range(1, 13):
        if i % 2 == 0:
            myTurtle.forward(distanceLength)
            myTurtle.left(90)
            myTurtle.forward(15)
            myTurtle.write(str(i))
            myTurtle.back(30)
            myTurtle.forward(15)
            myTurtle.right(90)
#draw the title at the top
def drawTitle(myTurtle):
    myTurtle.goto(0,300)
    myTurtle.write("Number of Students Sick Each Month", align='center', font=('Arial', 25, "normal"))
#stamp the image on the left
def stampImage(myTurtle, window):
    window.addshape('Students.gif')
    myTurtle.shape('Students.gif')
    window.mainloop()
#main function
def main():
    #create turtle
    bob = turtle.Turtle()
    wn = turtle.Screen()
    bob.speed(10)#slow speed. speed of is fast
    tupleHeights = []
    file = open("Heights.csv", "r")
    fileData = file.readline()
    listFileData = fileData.split(",") 
    for num in range(len(listFileData)):
        listFileData[num] = int(listFileData[num])
    tupleColors = ("#0320fc", "#0bfc03", "#50C7B5", "#C7C550", "#5065C7", "#eb34e5", "#3493eb", "#34eb99", "#eb3434", "#ebba34", "#a834eb", "#eb3462")
    tupleMonths = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")
    listBotRightXCoord = []
    listBotRighyYCoord = []
    width = 50
    #draw a bar/rect for each height
    repositionTurtle(bob, -400, -100, 90) 
    drawX(bob, 400)
    repositionTurtle(bob, -400, -100, 90)
    drawY(bob, 90, -300, 550)
    repositionTurtle(bob, -400, -100, 90)
    drawYAxTitles(bob)
    repositionTurtle(bob, -375, -100, 90)
    for i in range(len(listFileData)):
        makeRectangle(bob, listFileData[i], width, tupleColors[i])
        listBotRightXCoord.append(bob.xcor()) 
        listBotRighyYCoord.append(bob.ycor())
        repositionTurtle(bob, bob.xcor()+20, bob.ycor(), 90)
    labelBars(bob, listBotRightXCoord, listBotRighyYCoord, tupleMonths)
    bob.penup()
    drawTitle(bob)
    bob.goto(-460, 100)
    stampImage(bob, wn)
    wn.exitonclick() #last statement
main()
