# Building a Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Enter first number\n"))
for symbol in operations:
    print(symbol)
operational_symbol = input("Pick an operation from the line above.\t")
num2 = int(input("Enter second number\n"))
calculation_function = operations[operational_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operational_symbol} {num2} = {answer}")
