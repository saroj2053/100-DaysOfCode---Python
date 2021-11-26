# Pizza Order

print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
##cost_small = 15
##cost_medium = 20
##cost_large = 25
##if size == "S":
##    if add_pepperoni == "Y":
##        cost_small+=2
##        if extra_cheese == "Y":
##            cost_small+=1
##            print(f"Your final bill is: ${cost_small}")
##        else:
##            print(f"Your final bill is: ${cost_small}")
##    else:
##        print(f"Your final bill is: ${cost_small}")
##if size == "M":
##    if add_pepperoni == "Y":
##        cost_medium+=3
##        if extra_cheese == "Y":
##            cost_medium+=1
##            print(f"Your final bill is: ${cost_medium}")
##        else:
##            print(f"Your final bill is : ${cost_medium}")
##    else:
##        print(f"Your final bill is: ${cost_medium}")
##if size == "L":
##    if add_pepperoni == "Y":
##        cost_large+=3
##        if extra_cheese == "Y":
##            cost_large+=1
##            print(f"Your final bill is: ${cost_large}")
##        else:
##            print(f"Your final bill is: ${cost_large}")
##    else:
##        print(f"Your final bill is: ${cost_large}")
bill = 0
if size =="S":
    bill += 15
elif size =="M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
