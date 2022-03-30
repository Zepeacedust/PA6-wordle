import random
class Game:
    def __init__(self, length, guesses,word) -> None:
        self.length  = length
        self.guesses = guesses
        self.selected = word
        self.attempts = 0
        self.gameState = ""
        self.clues = []
    def save(self):
        return (self.guesses, self.gameState,self.length,self.selected,self.clues)
    def guess(self,attempt):
        if len(attempt) != self.length:
            print("incorrect length")
            return
        clue, correct = self.generate_clue(attempt.lower())
        self.clues.append((attempt, clue))
        if correct:
            self.gameState = "W"
        else:
            self.attempts += 1
            if self.attempts == self.guesses:
                self.gameState = "L"
        return clue
    def generate_clue(self,guess):
        clue = ""
        correct = True
        for i in range(self.length):
            if guess[i].lower() == self.selected[i].lower():
                clue += "C"
            elif guess[i].lower() in self.selected.lower():
                clue += "c"
                correct = False
            else:
                clue += "-"
                correct = False
        return (clue, correct)
