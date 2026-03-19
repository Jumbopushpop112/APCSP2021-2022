import csv
import turtle
def drawLine(bob, line):
    bob.goto(int(line[0]),int(line[1]))
def main():
    bob = turtle.Turtle()
    bob.hideturtle()
    bob.speed(0)
    wn = turtle.Screen()
    file = open("Points.csv", "r")
    csv_reader = csv.reader(file)
    listLines = []
    for line in csv_reader:
        listLines.append(line[0].split(" "))
    bob.penup()
    for x in range(len(listLines)):
        drawLine(bob, listLines[x])
        bob.pendown()
    wn.mainloop()
main()