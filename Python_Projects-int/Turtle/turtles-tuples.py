# A Turtle Walk Project involving the use of Tuples.

import random
import turtle as t
from turtle import Screen
jim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


directions = [0, 90, 180, 270]
jim.shape("turtle")
jim.pensize(15)
jim.speed("fastest")

for _ in range(200):
    jim.color(random_color())
    jim.forward(30)
    jim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

