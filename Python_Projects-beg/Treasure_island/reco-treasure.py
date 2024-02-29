# A recap of the Treasure-island project.

print("Welcome to the Treasure Hunt!\n")
print("All the best. Good luck!\n")
dir=input('Which direction would you like to move \n'
         '"Left" or "Right"? \n').lower()
if dir == "left":
  opt=input('Would you like to "swim" or "wait"? \n').lower()
  if opt == "wait":
    door=input('Which door would you like to pass through? \n'
              '"Red", "Yellow" or "Blue"? \n').lower()
    if door == "red":
      print("You have entered a room full of chillies. GAME OVER!\n")
    elif door == "blue":
      print("You have entered a room full of sharks. GAME OVER!\n")
    elif door == "yellow":
      print("Congratulations. You've won!\n")
    else:
      print("INVALID choce. Restart the game.\n")
  elif opt == "swim":
    print('You\'ve been electrocuted by an eel. GAME OVER!\n')
  else:
    print('INVALID choice. Restart the game!\n')
elif dir == "right":
  print('You\'ve been ambushed by pirates. GAME OVER!\n')
else:
  print("INVALID choice. Restart the game!\n")
