import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
score_user = 0
score_computer = 0
is_playing = True

while is_playing:

    should_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if should_start == 'y':
        def deal_card():
            for i in range(0, 2):
                user_cards.append(random.choice(cards))
            return user_cards

        def deal_with_computer_card():
            for i in range(0, 1):
                computer_cards.append(random.choice(cards))
            return computer_cards

        deal_card()
        deal_with_computer_card()
        print(f"Your cards: {user_cards}")
        print(f"Computer first card: {computer_cards}")

        choose_next_card = input("Do you want to pick another card? Type 'y' or 'n'. ")
        if choose_next_card == 'y':
            for _ in range(1):
                user_cards.append((random.choice(cards)))
            print(f"User_cards: {user_cards}")

        for _ in range(1):
            computer_cards.append(random.choice(cards))
        print(f"Computer cards: {computer_cards}")

        for scores in user_cards:
            score_user += scores
        print(f"User scores: {score_user}")

        for scores in computer_cards:
            score_computer += scores
        print(f"Computer scores: {score_computer}")

        def compare_scores(userscore, computerscore):
            if userscore > 21:
                print("You lose!")
            elif userscore > computerscore:
                print("You win!")
            elif userscore == computerscore:
                print("Draw")
            else:
                print("You lose!")
        compare_scores(userscore=score_user, computerscore=score_computer)
    else:
        print("Goodbye")

    repeat_again = input("Do you want to continue? Type yes or no. ")

    if repeat_again == 'no':
        is_playing = False
        print("Thanks for Playing")

