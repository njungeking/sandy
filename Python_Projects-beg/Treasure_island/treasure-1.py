# Treasure island project.

print("Welcome to treasure island!\n")
print("Your mission is to find the treasure!\n")
dir=input("Which direction would you like to go? \n"
         "'Left' or 'Right'? \n")
dir_low=dir.lower()
if dir_low == "left":
  opt=input("Do you wish to swim or wait? Type \n"
           "'Swim' or 'Wait': \n")
  opt_lower=opt.lower()
  if opt_lower == "wait":
    door=input("Which door would you like to pass through? \n"
         "Blue, Yellow or Red? Type 'Blue', 'Yellow' \n"
         "or 'Red': \n")
    door_lower=door.lower()
    if door_lower == "blue":
      print("You've entered a rooom full of beasts. GAME OVER!\n")
    elif door_lower == "red":
      print("You've entered a room full of fire ants. GAME OVER!\n")
    elif door_lower == "yellow":
      print("Congratulations. You've WON.\n")
    else:
      print("You were ambushed by pirates. GAME OVER!\n")
  elif opt_lower == "swim":
    print("You have been eaten by a Crocodile. GAME OVER!\n")
  else:
    print("You were ambushed by pirates. GAME OVER!\n")
else:
  print("You were ambushed by pirates. GAME OVER!\n")
