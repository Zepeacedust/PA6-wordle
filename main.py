import random
from game import Game
from loading_module import Word_Manager
from high_scores import Account_Manager

WORDS = Word_Manager()
ACCOUNT = Account_Manager()
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
    ACCOUNT.update(game)

def add_word():
    WORDS.update(input("Enter word to add: "))
def check_history():
    his = ACCOUNT.retrieve_data()
    if his == None:
        print("No games available")
    else:
        c = 1
        print("#--------------------------------------------------------#")
        for x in his:
            if x["state"] == "W":
                gen = "Won"
            else:
                gen = "lost"
            print("Game",c)
            print("You had",x["guesses"],"guesses")
            print("You",gen,"The game")
            print("And the word you where looking for was:",x["word"])
            print("#--------------------------------------------------------#")
            c += 1
        
def switch_accounts():
    ACCOUNT.log_in(input("enter account name(if it does not exist it will be created): "))

def main_menu():
    while True:
        if ACCOUNT.current == None:
            print("You are not logged in, press 4 to log in.")
        else:
            print(f"Hello {ACCOUNT.current}.")
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
ACCOUNT.exit()