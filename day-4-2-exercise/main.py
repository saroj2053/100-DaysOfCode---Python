import random

names_string = input("Give me everybody's names, separated by comma ,\n")
names = names_string.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} will pay the bill.")