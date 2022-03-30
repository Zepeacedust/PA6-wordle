import random
from game import Game
from loading_module import Word_Manager

WORDS = Word_Manager()
def play_game():
    guesses = int(input("How many guesses do you want? "))
    letters = int(input("How many letters do you want? "))
    word = WORDS.retrieve_word(letters)
    while word == None:
        print(f"No words of length {letters}")
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


while True:
    print()
    play_game()
        