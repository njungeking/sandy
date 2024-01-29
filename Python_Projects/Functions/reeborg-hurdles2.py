# Reeborg hurdles 2 project involving
# the use of while loops.

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    jump()
