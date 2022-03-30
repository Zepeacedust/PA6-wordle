import random
word_database_filename = "words.csv"

def load_words(filename) -> list:
    pass

WORDS = load_words(word_database_filename)


class Game:
    def __init__(self) -> None:
        self.selected = random.choice(WORDS)