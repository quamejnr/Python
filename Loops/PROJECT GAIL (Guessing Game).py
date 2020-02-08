secret_word = "APPLE"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
name_of_player = input("Enter your name: ")

print("WELCOME " + name_of_player.upper() + "! THIS IS A GUESSING GAME")
print("The rules are simple: You have three attempts and three clues to guess the secret word.\n")

while guess_word.casefold() != secret_word and not (out_of_guesses):
    if guess_count == 0:
        print("Clue 1: It is used as a symbol of love")
        guess_word = input("Enter guess word: ")
        guess_count += 1

    elif guess_count == 1:
        print("\nClue 2: Mostly favoured by Wicked stepmothers")
        guess_word = input("Enter guess word: ")
        guess_count += 1

    elif guess_count == 2:
        print("\nClue 3: It is a fruit")
        guess_word = input("Enter guess word: ")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("\nSorry " + name_of_player.upper() + " You are out of guesses, You lose!")
else:
    print("\nCongratulations "+name_of_player.upper()+ " You win!")

