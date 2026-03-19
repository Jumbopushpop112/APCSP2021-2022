import turtle
bob = turtle.Turtle()
def moveForward():
    bob.forward(10)
def moveBackward():
    bob.back(10)
def moveLeft():
    bob.left(90)
    bob.forward(10)
def moveRight():
    bob.right(90)
    bob.forward(10)
def main():
    window = turtle.Screen()
    #move the turtle forward
    bob.left(90)
    window.onkey(moveForward, "Up")
    #move the turtle backwards
    window.onkey(moveBackward, "Down")
    #move the turtle left
    window.onkey(moveLeft, "Left")
    #move the turtle right
    window.onkey(moveRight, "Right")
    #listen for key movement, set up window and set to exit canvas on click
    window.listen()
    window.setup(1920, 1000, 0, 0)
    window.exitonclick()
main()
