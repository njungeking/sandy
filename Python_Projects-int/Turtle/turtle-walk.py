# A Turtle Walk Project.

import random
from turtle import Turtle,Screen
jim = Turtle()
colors = ["black", "yellow", "brown", "red", "orange", "blue", "grey"]
directions = [0, 90, 180, 270]
jim.shape("turtle")
jim.pensize(15)
jim.speed("fastest")

for _ in range(200):
    jim.color(random.choice(colors))
    jim.forward(30)
    jim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()

