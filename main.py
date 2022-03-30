import random
from game import Game
from loading_module import Word_Manager

WORDS = Word_Manager()

def play_game():
    guesses = int(input("How many guesses do you want? "))
    letters = int(input("How many letters do you want? "))
    word = WORDS.retrieve_word(letters)
    while word == None:
        letters = int(input(f"No words of length {letters}, please enter another length: "))
        word = WORDS.retrieve_word(letters)
    game = Game(letters,guesses,word)
    while game.gameState == "":
        print(f"\nAttempts remaining: {game.guesses - game.attempts}")
        guess = input("Guess: ")
        print(guess)
        print(game.guess(guess))
    if game.gameState == "W":
        print("Congratulations, you have won!")
    else:
        print("out of guesses, lol get rekt nerd.")

def add_word():
    pass
def check_history():
    pass
def switch_accounts():
    pass

def main_menu():
    while True:
        print("1. Play a game")
        print("2. Add word")
        print("3. Check history")
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