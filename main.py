import sys
from turtle import *
from tkinter import *

root = Tk()
root.title("Art using Python")

canvas1 = Canvas(root, width=800, height=600)
trt_screen = TurtleScreen(canvas1)
canvas1.grid(row=0, columnspan=2)
exitBtn = Button(root, text="Exit", bg="red", command=lambda: sys.exit())
exitBtn.grid(row=1, column=0, pady=20)
drawBtn = Button(root, text="Draw", bg="green", command=lambda: main())
drawBtn.grid(row=1, column=1, pady=20)

trt = RawTurtle(trt_screen)

# Tree
def tree():
    # Tree trunk
    trt.color("saddlebrown")
    trt.begin_fill()
    for i in range(2):
        trt.forward(40)
        trt.left(90)
        trt.forward(10)
        trt.left(90)
    trt.end_fill()
    
    # Turn the turtle around
    trt.forward(10)
    trt.left(90)
    trt.forward(5)
    
    # Leaves on tree
    trt.color("forestgreen")
    trt.begin_fill()
    trt.circle(25)
    trt.end_fill()
    
    trt.right(90)

# Cloud
def cloud(X, Y):
    x = [X, X+6, X+2, X]
    y = [Y+4, Y+2, Y-2, Y]
    for x, y in zip(x, y):
        trt.penup()
        trt.goto(x, y)
        trt.pendown()
        trt.color("white")
        trt.begin_fill()
        trt.circle(20)
        trt.end_fill()
        trt.right(90)

def main():
    global trt, drawBtn
    drawBtn["state"] = "disable"
    trt.speed(0)
    trt_screen.bgcolor("skyblue")

    # Grass
    trt.penup()
    trt.goto(-400, -100)
    trt.pendown()
    trt.color("limegreen")
    trt.begin_fill()
    for i in range(2):
        trt.forward(800)
        trt.right(90)
        trt.forward(400)
        trt.right(90)
    trt.end_fill()

    # Left Mountain
    trt.penup()
    trt.goto(-400, -100)
    trt.pendown()
    trt.color("dimgray")
    trt.begin_fill()
    for i in range(3):
        trt.forward(300)
        trt.left(120)
    trt.end_fill()

    # Right Mountain
    trt.penup()
    trt.goto(100, -100)
    trt.pendown()
    trt.begin_fill()
    for i in range(3):
        trt.forward(300)
        trt.left(120)
    trt.end_fill()

    # Middle Mountain
    trt.penup()
    trt.goto(-160, -100)
    trt.pendown()
    trt.color("gray")
    trt.begin_fill()
    for i in range(3):
        trt.forward(400)
        trt.left(120)
    trt.end_fill()

    # Middle Mountain Ice Cap
    trt.penup()
    trt.goto(-35, 120)
    trt.pendown()
    trt.color("white")
    trt.begin_fill()
    trt.left(35)
    trt.forward(60)
    trt.right(90)
    trt.forward(30)
    trt.left(100)
    trt.forward(45)
    trt.right(85)
    trt.forward(65)
    trt.left(160)
    trt.forward(150)
    trt.end_fill()

    # Left Mountain Ice Cap
    trt.penup()
    trt.goto(-215, 100)
    trt.pendown()
    trt.color("snow")
    trt.begin_fill()
    trt.forward(70)
    trt.left(120)
    trt.forward(75)
    trt.left(150)
    trt.forward(45)
    trt.right(90)
    trt.forward(45)
    trt.left(120)
    trt.end_fill()

    # Right Mountain Ice Cap
    trt.penup()
    trt.goto(203, 80)
    trt.pendown()
    trt.begin_fill()
    trt.forward(95)
    trt.right(120)
    trt.forward(80)
    trt.right(150)
    trt.forward(50)
    trt.left(70)
    trt.end_fill()

    trt.left(50)

    # Sun
    trt.penup()
    trt.goto(-500, 350)
    trt.pendown()
    trt.color("yellow")
    trt.begin_fill()
    trt.circle(125)
    trt.end_fill()


    # Plant the second tree
    trt.penup()
    trt.goto(200,-150)
    trt.pendown()
    tree()

    # Plant the third tree
    trt.penup()
    trt.goto(300,-250)
    trt.pendown()
    tree()

    # Plant the fourth tree
    trt.penup()
    trt.goto(-300,-250)
    trt.pendown()
    tree()

    # Plant the fifth tree
    trt.penup()
    trt.goto(-200,-100)
    trt.pendown()
    tree()



    # House
    trt.penup()
    trt.goto(-100, -100)
    trt.pendown()
    trt.pensize(3)
    trt.color("chocolate", "orange") # (stroke, fill)
    trt.begin_fill()
    for i in range(4):
        trt.forward(100)
        trt.left(90)
    trt.end_fill()
    trt.left(90)

    trt.color("brown", "firebrick")

    # Chimney
    trt.penup()
    trt.goto(-27.5, -85)
    trt.pendown()
    trt.color("brown", "firebrick")
    trt.begin_fill()
    for i in range(2):
        trt.forward(20)
        trt.left(90)
        trt.forward(50)
        trt.left(90)
    trt.end_fill()

    # Roof
    trt.penup()
    trt.goto(-100, -100)
    trt.pendown()
    trt.begin_fill()
    for i in range(3):
        trt.forward(100)
        trt.left(120)
    trt.end_fill()


    # Dor
    trt.penup()
    trt.goto(-35, -200)
    trt.pendown()
    trt.color("red")
    trt.begin_fill()
    for i in range(2):
        trt.forward(25)
        trt.left(90)
        trt.forward(40)
        trt.left(90)
    trt.end_fill()
    trt.penup()
    trt.goto(-30, -185)
    trt.pendown()
    trt.color("black")
    trt.begin_fill()
    trt.circle(1)
    trt.end_fill()


    # Window
    trt.penup()
    trt.goto(-80, -190)
    trt.pendown()
    trt.color("black", "white")
    trt.begin_fill()
    for i in range(2):
        trt.forward(25)
        trt.left(90)
        trt.forward(40)
        trt.left(90)
    trt.end_fill()
    trt.penup()
    trt.goto(-67.5, -190)
    trt.pendown()
    trt.color("black")
    trt.begin_fill()
    trt.left(90)
    trt.forward(40)
    trt.end_fill()
    trt.penup()
    trt.goto(-57.5, -170)
    trt.pendown()
    trt.color("black")
    trt.begin_fill()
    trt.left(90)
    trt.forward(22)
    trt.end_fill()

    # Cloud
    cloud(-300, 200)
    cloud(-100, 250)
    cloud(-75, 250)
    cloud(210, 175)
    cloud(180, 175)


trt_screen.mainloop()