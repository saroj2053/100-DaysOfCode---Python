# # Randomisation
# import random
# import my_module
#
# print(my_module.pi)
#
#
# random_integer = random.randint(100, 150)
# print(f"Integer is {random_integer}")
#
# # 0.0000000000 - 0.999999999....
# random_float = random.random()
# print(random_float)
#
# dec = random_float * 5
# print(dec)

# Lists
states_of_india = ["Bihar", "Jharkhand", "West Bengal", "New Delhi", "Punjab", "Bengaluru"]
states_of_india.extend(['Odisha', 'Chhatisgarh'])
print(states_of_india)

# IndexErrors
num_of_states = len(states_of_india)
print(states_of_india[num_of_states - 1])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)