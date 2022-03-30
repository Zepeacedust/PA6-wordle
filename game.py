import random
class Game:
    def __init__(self, length, guesses,word) -> None:
        self.lenght  = length
        self.guesses = guesses
        self.selected = word
        self.attempts = 0
        self.gameStat = ""
    def save(self):
        pass
    def guess(self,attempt):
        if self.attempts == self.guesses:
            print("Max guesses reached")
            return
        if len(attempt) != self.lenght:
            print("incorrect length")
            return
        fin = ""
        count = 0
        for x in attempt.lower():
            if x == self.selected[count].lower():
                fin += "C"
            elif x in self.selected.lower():
                fin += "c"
            else:
                fin += "-"
            count += 1
        for x in fin:
            if x != "C":
                print(fin)
                self.attempts += 1
                return
        print(fin)
        print("Congrats you won!")
