import turtle
def drawTree(myTurtle, listX, listY, window):
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
    #top of branch
    myTurtle.forward(90)
    listX.append(myTurtle.xcor())
    listY.append(myTurtle.ycor())
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
def stampStar(myTurtle, window):
    window.addshape("Star (Resized).gif")
    myTurtle.shape("Star (Resized).gif")
    myTurtle.stamp()
def repositionTurtle(myTurtle, x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
def stampStar(myTurtle, listX, listY):
    myTurtle.penup()
    for i in range(len(listX)):
        myTurtle.goto(listX[i], listY[i])
        myTurtle.shape("Star (Resized).gif")
        myTurtle.stamp()
def stamp12Gifts(myTurtle, listX, listY, giftImages, window):
    myTurtle.penup()
    for i in range(len(listX)):
        myTurtle.goto(listX[i], listY[i]-100)
        window.addshape(giftImages[i])
        myTurtle.shape(giftImages[i])
        myTurtle.stamp()
def stampLeftGifts(myTurtle, listX, listY):
    myTurtle.penup()
    for i in range(len(listX)):
        myTurtle.goto(listX[i]-75, listY[i]-220)
        myTurtle.shape("Wrapped Gift 1 (Resized).gif")
        myTurtle.stamp()
def stampRightGifts(myTurtle, listX, listY):
    myTurtle.penup()
    for i in range(len(listX)):
        myTurtle.goto(listX[i] + 95, listY[i] - 220)
        myTurtle.shape("Wrapped Gift 2 (Resized).gif")
        myTurtle.stamp()
def main():
  giftImages = ['Partridge in A Pear Tree (Resized).gif', 'Two Turtle Doves (Resized).gif',
                  'Three French Hens (Resized).gif', 'Four Calling Birds (Resized).gif',
                  'Five Gold Rings (Resized).gif', 'Six Geese A-Laying (Resized).gif',
                  'Seven Swans A-Swimming (Resized).gif', 'Eight Maids A-Milking (Resized).gif',
                  'Nine Ladies Dancing (Resized).gif', 'Ten Lords A-Leaping (Resized).gif',
                  'Eleven Pipers Piping (Resized).gif', 'Twelve Drummers Drumming (Resized).gif']
  window = turtle.Screen()
  window.setup(1920,1000,0,0)
  window.addshape("Star (Resized).gif")
  bob = turtle.Turtle()
  bob.speed(65)
  listXCor = []
  listYCor = []
  x = -600
  #first row
  for i in range(4):
      repositionTurtle(bob, x + (i*350), 175)
      drawTree(bob, listXCor, listYCor, window)
  #second row
  for i in range(4):
      repositionTurtle(bob, x + (i * 350), -95)
      drawTree(bob, listXCor, listYCor,window)
  #third row
  for i in range(4):
      repositionTurtle(bob, x + (i * 350), -365)
      drawTree(bob, listXCor, listYCor, window)
  stamp12Gifts(bob, listXCor, listYCor, giftImages, window)
  stampStar(bob, listXCor, listYCor)
  window.addshape("Wrapped Gift 1 (Resized).gif")
  stampLeftGifts(bob, listXCor, listYCor)
  window.addshape("Wrapped Gift 2 (Resized).gif")
  stampRightGifts(bob, listXCor, listYCor)
  stampStar(bob, listXCor, listYCor)
  window.exitonclick()
main()
