# A sample Class Project.

class DetailsPupils:
    def __init__(self, name, identification):
        self.name = name
        self.id = identification
        self.followers = 0


students = DetailsPupils("Paul", "55")

print(students.name)
print(students.id)
print(students.followers)

