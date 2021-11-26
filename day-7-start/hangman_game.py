import random

lives = 6
coc_characters = ["archer", "barbarian", "miner", "giant", "dragon", "goblin", "witch", "bowler"]
chosen_coc_character = random.choice(coc_characters)

display = []
for i in range(len(chosen_coc_character)):
    display += "_"
print(display)

isRunning_Game = False

while not isRunning_Game:
    guess = input("Please make a guess of letter \n").lower()

    # Checking the guessed letter which is typed by the user
    for position in range(len(chosen_coc_character)):
        letter = chosen_coc_character[position]
        if letter == guess:
            display[position] = letter

    # In case we cannot find the guessed letter in the word chosen by random module
    if guess not in chosen_coc_character:
        lives = lives - 1
        if lives == 0:
            isRunning_Game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        isRunning_Game = True
        print("You win!")
