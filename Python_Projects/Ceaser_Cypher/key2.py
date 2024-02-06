# Another attempt on functions involving
# the use of keyword arguments.

def greet_tp(name,place,time):
  print(f"Hello {name}!")
  print(f"How is {place}!")
  print(f"Is it {time} in {place}, {name}?")
  print(f"Thank you, {name}!")

greet_tp(time="9:00 am", name="Oscar", place="Melbourne")
