from turtle import *
import turtle
a = 0
b = 1
arrow = Turtle()
arrow.speed(0)
arrow.pencolor("purple")


for i in range(150):
    arrow.forward*5
    arrow.right(90)

a,b = b, a+b

turtle.done()