# Functions with Inputs

def greet(name, location):
    print(f"Hello, {name}")
    print(f"How do you do {name}?")
    print(f"Are you from {location}?")


greet("Saroj", "Ishworpur")


def cities(city_name):
    print(f"The city is: {city_name}")
    print(f"{city_name} is beautiful")


cities('Dusseldorf')

# Positional Arguments vs Keyword Arguments


def greet_with(name_of_person, where_from):
    print(f"Hello, {name_of_person}")
    print(f"What is like in {where_from}")


greet_with(where_from="Germany", name_of_person="Saroj")
