# Hangman Exercise
# Version 2

import random

word_list = ["Aardvark", "baboon", "camel", "donkey"]
chosen_word = random.choice(word_list)

# Testing Code
print(f"Your solution is: \n {chosen_word}")

guess = input("Guess a letter \n").lower()

display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)