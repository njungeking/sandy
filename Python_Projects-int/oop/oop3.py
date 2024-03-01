# Another round of modifying object attributes and calling methods.

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Country", ["Kenya", "Uganda", "Tanzania", "Nigeria", "Rwanda"])
table.add_column("Capital City", ["Nairobi", "Kampala", "Dodoma", "Abuja", "Kigali"])
table.align = "c"
print(table)
