# lists, dictionary, set, tuple

cities = ["Kigoma", "Kigali", "Kinshasa", "Kisumu", "Dodoma", "Nairobi", "Bujumbura"]
scores = [56, 67, 43, 67, 78, 90, 34]

car = {
    "make": "Toyota",
    "model": "Probox",
    "year": 2017,
    "gear": "Manual",
    "color": "White",
    "owners": ["Jane", "Jerry", "Miry"]
}

friends = {"Mike", "Walid", "Ahmed", "John", "Mike", "Walid"}  # unique elements

workers = ("Jane", "Jack", "Jim")  # tuple never change it programmatically

print(cities)
print(car)
print(friends)
print(workers)

print(cities[0])
print(cities[-2])  # last

print(car["model"])
print(car["color"])

# loop
for city in cities:  # for each city in cities
    print(city)

for key, value in car.items():
    print(key, value)

print(cities[1:-3])
cities.sort(reverse=True)
print(cities)



