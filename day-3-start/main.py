# print("Welcome to the rollercoaster")
# height = int(input("Enter your height in cm:"))
# if height > 120:
#     print("You can ride the rollercoaster")
# elif height == 120:
#     print("Luckily you are well enough for the ride")
# else:
#     print("Sorry you can't, you have to grow taller to ride.")

# Comparison Operators <, >, <=, >=
# = -> Assignment
# == -> Comparison


# Nested If/Else
'''
print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm:"))
if height >= 120:
    age = int(input("Enter your age: "))
    if age < 12:
        print("The ticket costs $5")
    elif age <= 18:
        print("You pay $7")
    else:
        print("The ticket costs $12")

else:
    print("Sorry you can't, you have to grow taller to ride.")
'''

# Multiple IF Statements
print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm:"))
if height >= 120:
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
        print("You can have a free ride!")
    else:
        bill = 12
    wants_photo = input("Do you want your photo to be taken? Y or N. ")
    if wants_photo == 'N':
        print(f"You pay ${bill}")
    elif wants_photo == 'Y':
        bill += 3
        print(f"Final bill is of ${bill}")