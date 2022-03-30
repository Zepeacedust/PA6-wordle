import random
from game import Game
from loading_module import Word_Manager

WORDS = Word_Manager()

while True:
    guesses = int(input("How many guesses do you want? "))
    letters = int(input("How many letters do you want? "))
    word = WORDS.retrieve_word(letters)
    while word == None:
        print(f"No words of length {letters}")
        word = WORDS.retrieve_word(letters)
    game = Game(guesses,letters,word)
    
        