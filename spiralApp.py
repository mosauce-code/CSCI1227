#This program draws a spiral using turtle graphics. 

import turtle
from math import pi
t = turtle.Turtle()
spiral = turtle.Screen()
spiral.bgcolor("black")
spiral.title("Spiral")
t.speed(10)
t.width(2)
t.penup()
t.goto(10,1)
t.pendown()
for i in range(10000):
    t.forward(1000 * pi *i / 360)
    t.right(840)
    if i % 2 == 0:
        t.color("red")
    else:
        t.color("blue")
turtle.done()

