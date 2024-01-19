# Treasure island project.

print("Welcome to treasure island!\n")
print("Your mission is to find the treasure!\n")

dir=input("Which direction would you like to \n"
         "go to: 'Left' or 'Right'? \n")
dir_low=dir.lower()
if dir_low == "left":
  opt=input("Would you like to 'Swim' or 'Wait'? \n")
  opt_low=opt.lower()
  if opt_low == "wait":
    door=input("Which door would you like to pass through: \n"
              "'Red', 'Yellow' or 'Blue'? \n")
    door_low=door.lower()
    if door_low == "red":
      print("You have entered a room full of fire. GAME OVER!\n")
    elif door_low == "blue":
      print("You have entered a flooding room. GAME OVER!\n")
    elif door_low == "yellow":
      print("Congratulations! You have WON!\n")
    else:
      print("You have been caught by pirates. GAME OVER!\n")
  elif opt_low == "swim":
    print("You have been electrocuted by an eel. GAME OVER!\n")
  else:
    print("You were have been caught by pirates. GAME OVER!\n")
else:
  print("You have been caught by pirates. GAME OVER!\n")
