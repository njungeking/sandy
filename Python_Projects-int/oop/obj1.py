# Constructing objects and accessing their attributes and methods.

#import turtle
#oscar = turtle.Turtle()

from turtle import Turtle, Screen
oscar = Turtle()
print(oscar)
oscar.shape("turtle")
oscar.color("DarkBlue")
oscar.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
