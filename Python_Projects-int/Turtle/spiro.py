# A Spirograph Project involving the use of the turtle package as well as tuples.

import random
import turtle as t
from turtle import Screen
jim = t.Turtle()
t.colormode(255)
jim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()

