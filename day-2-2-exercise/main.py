height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

h = float(height)
w = float(weight)
bmi = (w / (h * h)) # h * h can also be given as h ** 2
print(bmi)