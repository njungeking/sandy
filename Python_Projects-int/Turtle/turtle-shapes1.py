# Turtle Project #4.

from turtle import Turtle, Screen
import random

johnny = Turtle()
color = ["black", "yellow", "red", "green", "blue", "orange", "grey"]


def draw(num_sides):
    angle = 360 / num_sides
    for n in range(num_sides):
        johnny.forward(100)
        johnny.right(angle)


for shape_sides in range(3, 11):
    johnny.color(random.choice(color))
    draw(shape_sides)

screen = Screen()
screen.exitonclick()

