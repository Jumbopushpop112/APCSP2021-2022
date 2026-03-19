import turtle #grabbing all functionality of the turtle module

#create a turtle named Alex
alex = turtle.Turtle()
alex.shape("turtle")

#draw a square
alex.penup()
alex.goto(200, 150)
alex.pendown() 
alex.forward(200)
alex.left(90)
alex.forward(200) 
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)

#move turtle again for triangle
alex.penup()
alex.goto(-100,100)
alex.pendown()
alex.setheading(180) #this faces the turtle left 
