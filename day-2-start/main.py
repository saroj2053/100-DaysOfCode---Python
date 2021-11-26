# Primitive Data Types

# String
print("Munchen"[0])
print("Munchen"[-1])

print("Berlin" + "Munchen")
print("123" + "345")

# Integers
156
print(type(123))
print(type(123_456_789))  # the number is recognised same as 123,456,789

# Floats
3.14156
25.93
print(type(22/7))

# Boolean
True
False

# Type Error, Type Checking and Type Conversion
# We use type() to investigate the data type we are working in

# numChar = len(input("Enter your name:"))
# # print("Your name has" + numChar + " characters.") Gives TypeError as numChar is of int type
# print(type(numChar))
# # To print we have to typecast numChar into str
# num_char = str(numChar)
# print("Your name has " + num_char + " characters.")

cost1 = "23.44"
cost2 = "55.03"
sum_cost = float(cost1) + float(cost2)
print(sum_cost)

print(70 + float("23.90"))

# Mathematical Operations
8 + 6
9 - 3
8 / 4
7 * 8
2 ** 5
# 8 // 3  // -> Floor division

print(type(8 / 4))
print(2 ** 5)

# PEMDAS
# PARENTHESIS
# EXPONENTIATION
# MULTIPLICATION,DIVISION
# ADDITION,SUBTRACTION
# ()
# **
# * /
# + -
print(3 * 3 + 3 / 3 - 3)

print(4 ** 4 + 4 / 4 - 4)

# Number Manipulation and F Strings
print(round(8/3, 2))
num1 = 8 // 3
print(num1)
print(type(num1))

score = 1
score += 1 # Shorthand representation for score = score + 1

score = 0
height = 1.8
isWinning = True
# f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
