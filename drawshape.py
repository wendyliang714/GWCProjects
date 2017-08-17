from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

#Draw a square.
for square in range(4):
    t.pencolor("orange")
    t.forward(200)
    t.left(90)

#Draw a triangle.
for triangle in range(3):
    t.pencolor("green")
    t.backward(200)
    t.left(120)

#Draw any polygon with any color.
num_sides = int(input("How many sides?"))
color=input("What color would you like?")
side_length = 70
angle = 360 / num_sides

for polygon in range(num_sides):
    t.pencolor(color)
    t.forward(side_length)
    t.right(angle)

# Close window on click.
exitonclick()
