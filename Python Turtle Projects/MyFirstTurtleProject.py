import turtle #Grabbing the turtle module

canvas = turtle.Screen() #creates a canvas to draw upon

alex = turtle.Turtle() #create a turtle named Alex
#set the attributes of the turtle 
alex.shape("turtle")
alex.speed(6)
alex.pensize(1)
#make sure to end the fill
#turtle draws the shapes according to the code 
def drawSquare(f, red, ff): 
#draw the square
    alex.fillcolor(red) 
    alex.begin_fill()
    alex.forward(f) 
    alex.right(90)
    alex.forward(ff)
    alex.right(90)
    alex.forward(f)
    alex.right(90)
    alex.forward(ff)      
    alex.end_fill() 
    alex.penup()
    alex.forward(ff)
def drawTriangle(f, yellow, l): 
#draw the triangle
    alex.pendown() 
    alex.fillcolor(yellow)
    alex.begin_fill()
    alex.forward(f) 
    alex.left(l)
    alex.forward(f)
    alex.left(l)
    alex.forward(f) 
    alex.penup()
    alex.forward(f)
    alex.end_fill()  

def drawStar(f, blue, r):
#draw the star
    alex.penup()
    alex.goto(-10,-300) 
    alex.pendown() 
    alex.fillcolor(blue)
    alex.begin_fill()
    for i in range(5):
        alex.forward(100)  
        alex.right(144)
    alex.end_fill()
    
def drawPentagon(f, orange, r):
#draw the pentagon
    alex.penup()
    alex.goto(-300, 100) 
    alex.pendown() 
    alex.fillcolor(orange)
    alex.begin_fill() 
    for i in range(5):
       alex.forward(f) 
       alex.right(r) 
    alex.end_fill()
def drawTrapezoid(r, f, purple, rr, ff, rrr, fff, black):
#draw the trapezoid
    alex.penup()
    alex.goto(-300, 225) 
    alex.pendown()
    alex.right(r)
    alex.fillcolor(purple)
    alex.begin_fill() 
    alex.forward(f)
    alex.right(rr)
    alex.forward(ff)
    alex.right(rrr)
    alex.forward(ff)
    alex.right(55) 
    alex.forward(fff) 
    alex.end_fill()
    alex.penup()
    alex.fillcolor(black)
    alex.goto(0,0)
def main():
#main function that hosts all the other functions 
    drawSquare(300, "red", 200)  
    drawTriangle(200, "yellow", 120) 
    drawStar(100, "blue", 144)
    drawPentagon(100, "orange", 72) 
    drawTrapezoid(120,200, "purple", 130, 100, 50, 95, "black") 
    canvas.exitonclick() 
main()   
 
 
 
