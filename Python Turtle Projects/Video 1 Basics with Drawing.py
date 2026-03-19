import turtle
#create canvas
canvas = turtle.Screen()

#create a turtle to do the drawing
myTurtle = turtle.Turtle()


#get default x and y coords
x = myTurtle.xcor()
y = myTurtle.ycor()
print (f"({x}, {y})") #printing the coordinates
#draw a line
myTurtle.forward(100)

myTurtle.shape("turtle")
myTurtle.penup()
myTurtle.goto(0,-20)
myTurtle.pendown()
myTurtle.pencolor("blue")
myTurtle.pensize(10)
myTurtle.forward(100)
myTurtle.left(60)
myTurtle.forward(100)

#exit/close window upon clicking it
canvas.exitonclick()
