# Addition of dictionaries to a list project.

travel_log = [
{
  "country": "Germany",
  "cities": ["Koln", "Cologne", "Berlin", "Stutgutt"],
  "towns": 64,
},
{
  "country": "Kenya",
  "cities": ["Nairobi", "Kisumu", "Mombasa", "Nakuru"],
  "towns": 55,
},
]

print("Welcome to a Travel log program!\n")

def new_country(country, cities, towns):
  new = {}
  new["country"] = country
  new["cities"] = cities
  new["towns"] = towns
  travel_log.append(new)

new_country("USA", ["New Jersey", "Chicago", "Santa Fe", "Arizona"], 23)
print(travel_log)
