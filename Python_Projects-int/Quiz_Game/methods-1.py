# An introduction to methods.

class IgUser:
    print("Welcome to an Instagram User checking program!")

    def __init__(self, name, id):
        self.name = name
        self.identity = id
        self.followers = 0
        self.following = 0

    def count(self, person):
        person.followers += 1
        self.following += 1


person_1 = IgUser("Oscar", "21")
person_2 = IgUser("Paul", "72")

print(person_1.name)
print(person_1.identity)
print(person_1.followers)
print("\n")
print(person_2.name)
print(person_2.identity)
print(person_2.followers)
print("\n")
person_1.count(person_2)
person_2.count(person_1)
print(person_1.followers)
print(person_1.following)
print(person_2.followers)
print(person_2.following)

