# Project On Treasure Island
print('''
    Welcome to the Treasure Island.
    Your mission is to find the treasure.''')

direction = input("You are at a cross road.Do you want to go left or right? Type 'left' or 'right' \n")
if direction.lower() == 'right':
    print("You slipped into a hole. Game Over...")
elif direction.lower() == 'left':
    swim_boat = input("Do you want to swim or wait for the boat? Type 'swim' or 'wait' \n")
    if swim_boat.lower() == 'swim':
        print("You ended up in a crocodile's mouth. Game Over.")
    elif swim_boat.lower() == 'wait':
        door = input('''You came to an island safely.
         There are three doors of three different colours. 
         Pick among Yellow , Blue or Red \n''')
        if door.lower() == 'blue' or door.lower() == 'red':
            print("You come across room of beasts. game over..")
        elif door.lower() == 'yellow':
            print("You Win")