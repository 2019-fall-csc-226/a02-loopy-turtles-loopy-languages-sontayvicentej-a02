# Author: sontayvicentej
# Username: sontayvicentej
# Assignment: A02: Loopy Turtles

import turtle
wn = turtle.Screen()
jhonny = turtle.Turtle()
another = turtle.Turtle()
jhonny.color()

def square(t, distance):
    """ Draws a square"""
    for k in ["red", "yellow", "orange", "blue"]:
        t.color(k)
        t.forward(distance)
        t.left(90)


for i in range(3):
    jhonny.forward(80)
    jhonny.left(36)
    for i in range(3):
        jhonny.forward(80)
        jhonny.left(36)


size = 15
for i in range(10):
    square(jhonny, 76)
    size = size+15
    jhonny.forward(80)
    jhonny.left(36)

wn.exitonclick()

