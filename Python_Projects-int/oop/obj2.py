# Practicing the modification of object attributes and calling methods.

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Table", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
