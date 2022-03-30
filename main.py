import random
from game import Game
from loading_module import Word_Manager
from high_scores import Account_Manager


def get_integer(message):
    output = input(message)
    while not output.isdigit():
        output = input("That is not a valid integer, please try again: ")
    return int(output)


WORDS = Word_Manager()
ACCOUNT = Account_Manager()


def play_game():
    #determine starting variables
    guesses = get_integer("How many guesses do you want? ")
    letters = get_integer("How many letters do you want? ")
    
    word = WORDS.retrieve_word(letters)
    
    while word == None:
        letters = get_integer(
            f"No words of length {letters}, please enter another length: ")
        word = WORDS.retrieve_word(letters)
    #start the game
    game = Game(letters, guesses, word)
    #play the game
    while game.gameState == "":
        print(f"\nAttempts remaining: {game.guesses - game.attempts}")
        guess = input("Guess: ")
        print(guess)
        print(game.guess(guess))
    if game.gameState == "W":
        print("Congratulations, you have won!")
    else:
        print("Out of guesses, you have lost.")
    ACCOUNT.update(game)


def add_word():
    WORDS.update(input("Enter word to add: "))


def check_history():
    print(ACCOUNT.retrieve_data())


def switch_accounts():
    ACCOUNT.log_in(
        input("enter account name(if it does not exist it will be created): "))


def main_menu():
    while True:
        if ACCOUNT.current == None:
            print("You are not logged in, progress will not be saved, press 4 to log in.")
        else:
            print(f"Hello {ACCOUNT.current}.")
        print("1. Play a game")
        print("2. Add word")
        print("3. Check history")
        if ACCOUNT.current == None:
            print("4. Log in")
        else:
            print("4. Switch account")
        print("5. Quit")
        a = input("What do you want to do? ")
        if a == "1":
            play_game()
        elif a == "2":
            add_word()
        elif a == "3":
            check_history()
        elif a == "4":
            switch_accounts()
        elif a == "5":
            break
        else:
            print("incorrect input")


main_menu()

WORDS.exit()
ACCOUNT.exit()
