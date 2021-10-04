from turtle import *
from tkinter import *


bgcolor("skyblue")

# Grass
penup()
goto(-400, -100)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()

# Left Mountain
penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# Right Mountain
penup()
goto(100, -100)
pendown()
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# Middle Mountain
penup()
goto(-160, -100)
pendown()
color("gray")
begin_fill()
for i in range(3):
    forward(400)
    left(120)
end_fill()

# Middle Mountain Ice Cap
penup()
goto(-35, 120)
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

# Left Mountain Ice Cap
penup()
goto(-215, 100)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()

# Right Mountain Ice Cap
penup()
goto(203, 80)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
left(70)
end_fill()

left(50)

# Sun
penup()
goto(-500, 350)
pendown()
color("yellow")
begin_fill()
circle(125)
end_fill()

# Tree
def tree():
    # Tree trunk
    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()
    
    # Turn the turtle around
    forward(10)
    left(90)
    forward(5)
    
    # Leaves on tree
    color("forestgreen")
    begin_fill()
    circle(25)
    end_fill()
    
    right(90)

# Cloud
def cloud(X, Y):
    x = [X, X+6, X+2, X]
    y = [Y+4, Y+2, Y-2, Y]
    for x, y in zip(x, y):
        penup()
        goto(x, y)
        pendown()
        color("white")
        begin_fill()
        circle(20)
        end_fill()
        right(90)


def house(X, Y):
    pass


# Plant the second tree
penup()
goto(200,-150)
pendown()
tree()

# Plant the third tree
penup()
goto(300,-250)
pendown()
tree()

# Plant the fourth tree
penup()
goto(-300,-250)
pendown()
tree()

# Plant the fifth tree
penup()
goto(-200,-100)
pendown()
tree()



# House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "orange") # (stroke, fill)
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
left(90)

color("brown", "firebrick")

# Chimney
penup()
goto(-27.5, -85)
pendown()
color("brown", "firebrick")
begin_fill()
for i in range(2):
    forward(20)
    left(90)
    forward(50)
    left(90)
end_fill()

# Roof
penup()
goto(-100, -100)
pendown()
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()


# Dor
penup()
goto(-35, -200)
pendown()
color("red")
begin_fill()
for i in range(2):
    forward(25)
    left(90)
    forward(40)
    left(90)
end_fill()
penup()
goto(-30, -185)
pendown()
color("black")
begin_fill()
circle(1)
end_fill()


# Window
penup()
goto(-80, -190)
pendown()
color("black", "white")
begin_fill()
for i in range(2):
    forward(25)
    left(90)
    forward(40)
    left(90)
end_fill()
penup()
goto(-67.5, -190)
pendown()
color("black")
begin_fill()
left(90)
forward(40)
end_fill()
penup()
goto(-57.5, -170)
pendown()
color("black")
begin_fill()
left(90)
forward(22)
end_fill()

# Window Cross - Horizontal Line 
# penup()
# goto(0, 25)
# pendown()
# color("black")
# forward(25)



# Cloud
cloud(-300, 200)
cloud(-100, 250)
cloud(-75, 250)
cloud(210, 175)
cloud(180, 175)



hideturtle()
exitonclick()