import turtle
def drawTree(myTurtle, listX, listY):
    myTurtle.fillcolor("brown2")
    #make base of the tree
    myTurtle.begin_fill()
    myTurtle.penup()
    myTurtle.pendown()
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.end_fill()
    myTurtle.fillcolor("green")
    myTurtle.begin_fill()
    myTurtle.forward(100)
    myTurtle.backward(100)
    myTurtle.left(90)
    myTurtle.forward(150)
    myTurtle.left(150)
    myTurtle.forward(80)
    myTurtle.right(140)
    myTurtle.forward(50)
    myTurtle.left(135)
    myTurtle.forward(70)
    myTurtle.right(110)
    myTurtle.forward(35)
    myTurtle.left(115)
    myTurtle.forward(90)
    myTurtle.left(60)
    myTurtle.forward(90)
    myTurtle.left(110)
    myTurtle.forward(35)
    myTurtle.right(110)
    myTurtle.forward(50)
    myTurtle.left(115)
    myTurtle.forward(50)
    myTurtle.right(120)
    myTurtle.forward(80)
    myTurtle.left(155)
    myTurtle.forward(103)
    myTurtle.end_fill()
    myTurtle.hideturtle()
def repositionTurtle(myTurtle, x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
def main():
  window = turtle.Screen()
  window.setup(1920,1000,0,0)
  bob = turtle.Turtle()
  bob.speed(15)
  listXCor = []
  listYCor = []
  x = -600
  #first row
  for i in range(12):
      repositionTurtle(bob, x + (i*350), 175)
      drawTree(bob, listXCor, listYCor)
  #second row
  for i in range(4):
      repositionTurtle(bob, x + (i * 350), -95)
      drawTree(bob, listXCor, listYCor)
  #third row
  for i in range(4):
      repositionTurtle(bob, x + (i * 350), -365)
      drawTree(bob, listXCor, listYCor)
  window.exitonclick()
main()
