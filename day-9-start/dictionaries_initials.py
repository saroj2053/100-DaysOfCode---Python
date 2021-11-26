# Python Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary

# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."


# Creating an empty dictionary

dict1 = {}

# Wiping existing dict
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dict
programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary)

# Loop through the dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nested Lists and Dictionaries

capitals = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
# travel_log = {
#     "India": ["Bhagalpur", "Kanpur", "Nagpur"],
#     "Germany": ["Nuremberg", "Hamburg", "Dusseldorf"]
# }

# Nesting a dictionary in a dictionary
travel_log = {
    "India": {"cities_visited": ["Hyderabad", "Chandigarh", "Pune"], "total_visits": 10},
    "Nepal": {"cities_visited": ["kathmandu", "Birgunj", "Biratnagar"], "total_visits": 8}
}
print(travel_log)

# Nesting a dictionary in a list
travel_log = [
    {"country": "India",
     "cities_visited": ["Hyderabad", "Chandigarh", "Pune"],
     "total_visits": 10
    },
    {
    "country": "Nepal",
    "cities_visited": ["kathmandu", "Birgunj", "Biratnagar"],
    "total_visits": 8
    },
]