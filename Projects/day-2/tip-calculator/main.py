print("Welcome to the tip calculator.")
bill_amt = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_amt = ((100 + tip_percent) * bill_amt) / 100
num_people = int(input("How many people to split the bill?"))
shareable_amt = round(total_amt / num_people, 2)
print(f"Each person should pay: ${shareable_amt}")
