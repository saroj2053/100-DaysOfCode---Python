# Hangman Exercise
# Version 2

import random

word_list = ["aardvark", "baboon", "camel", "donkey"]
chosen_word = random.choice(word_list)

# Testing Code
print(f"Your solution is: \n {chosen_word}")


display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter \n").lower()

    # Checking guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
