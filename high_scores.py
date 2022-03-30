import glob
def load_file(filename):
    with open(filename, "r") as file:
        lines =  file.read().split("\n\n")
    games = []
    print("yeetus")
    for line in lines:
        if line == "":
            return games
        parts = line .split("\n")
        game = {}
        game["guesses"] = parts.pop(0)
        game["state"] = parts.pop(0)
        game["length"] = parts.pop(0)
        game["word"] = parts.pop(0)
        clues = []
        while parts != []:
            clues.append((parts.pop(0),parts.pop(0)))
        game["clues"] = clues
        games.append(game)
def get_valid_files():
    #finna öll leyfð files í words
    allowed = set()
    for file in glob.glob("accounts/*.csv"):
        try:
            allowed.add(file[9:][:-4])
        except Exception as e:
            print(f'invalid filename: "{file}" in words folder')
    return allowed

def overwrite_file(filename,data):
    with open(filename, "w") as file:
        for game in data:
            file.write(str(game["guesses"])+"\n")
            file.write(str(game["state"])+"\n")
            file.write(str(game["length"])+"\n")
            file.write(str(game["word"])+"\n")
            for guess in game["clues"]:
                file.write(guess[0]+"\n")
                file.write(guess[1]+"\n")
        file.write("\n")

class Account_Manager:
    def __init__(self):
        self.allowed = get_valid_files()
        self.loaded = dict()
        self.updated = set()
        self.current = None
    def retrieve_data(self):
        if self.current == None:
            return None
        #if account has been loaded before
        if self.current in self.loaded:
            #then return account data
            return self.loaded[self.current]
        #else try to load it
        if self.load(self.current):
            return self.loaded[self.current]
            #then return account data
    def load(self,account):
        if not account in self.allowed:
            return False
        self.loaded[account] = load_file(f"accounts/{account}.csv")
        return True
        
    def update(self, game):
        if self.current == None:
            return
        self.updated.add(self.current)
        if self.current in self.loaded:
            self.loaded[self.current].append(game.save())
        else:
            self.loaded[self.current] = [game.save()]
    def log_in(self, account):
        self.current = account
    def exit(self):
        for account in self.updated:
            overwrite_file(f"accounts/{account}.csv", self.loaded[account])
