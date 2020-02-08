import random
def ludu_game():

    dice_roll = random.randint(1, 6)
    while dice_roll != 6:
        print (dice_roll)
        dice_roll = random.randint(1,6)
    if dice_roll == 6:
            print (dice_roll)
            print("Player 1. Your Journey Begins")

    dice_roll = random.randint(1,6)
    while dice_roll ==6:
        print (dice_roll)
        dice_roll = random.randint(1,6)
    if dice_roll !=6:
        print(dice_roll)
        print("Player 2's turn")
print(ludu_game())

