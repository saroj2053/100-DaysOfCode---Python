# Adding Evens

total = 0

for i in range(0, 101):
    if i % 2 == 0:
        total += i

print(f"The sum is: {total}")

# Alternative

total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(total2)