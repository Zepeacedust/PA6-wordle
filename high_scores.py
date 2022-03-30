import glob
def load_file(filename):
    with open(filename, "r") as file:
        return file.read().split(",")
def get_valid_files():
    #finna öll leyfð files í words
    allowed = set()
    for file in glob.glob("accounts/*.csv"):
        try:
            allowed.add(int(file[9:][:-4]))
        except Exception as e:
            print(f'invalid filename: "{file}" in words folder')
    return allowed

def overwrite_file(filename,data):
    with open(filename, "w") as file:
        for game in data:
            file.write(str(game[0])+"\n")
            file.write(str(game[1])+"\n")
            file.write(str(game[2])+"\n")
            file.write(str(game[3])+"\n")
            for guess in game[4]:
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
        self.loaded[account] = load_file(f"account/l{account}.csv")
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
