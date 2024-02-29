# A recap of the Treasure-map project
# involving the use of nested lists.

row1=["✅","✅","✅"]
row2=["✅","✅","✅"]
row3=["✅","✅","✅"]
maps=[row1,row2,row3]
print("Welcome to a Treasure map game!\n")
print(f"{row1}\n{row2}\n{row3}")
position=input("Please enter the place where you \n"
              "wish to place the treasure: \n")
c=int(position[0])
r=int(position[1])
maps[r-1][c-1]='X'
print(f"{row1}\n{row2}\n{row3}")
