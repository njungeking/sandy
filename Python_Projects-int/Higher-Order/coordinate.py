# An introduction to the turtle coordinate system.

from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter the color: ")
colors = ["red", "green", "purple", "blue", "yellow", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()

