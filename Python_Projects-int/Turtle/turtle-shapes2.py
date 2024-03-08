# Another attempt at the Turtle shapes Project.

from turtle import Turtle, Screen
import random

pol = Turtle()
colors = ["black", "green", "red", "brown", "blue", "pink", "purple"]


def shape(shape_sides):
    angle = 360 / sides
    for turns in range(sides):
        pol.forward(100)
        pol.right(angle)


for sides in range(3, 11):
    pol.color(random.choice(colors))
    shape(sides)

screen = Screen()
screen.exitonclick()

