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
        file.write(",".join(data))

class Account_Manager:
    def __init__(self):
        self.allowed = get_valid_files()
        self.loaded = dict()
        self.updated = set()
    def retrieve_data(self,account):
        #if account has been loaded before
        if account in self.loaded:
            #then return account data
            return self.loaded[account]
        #else try to load it
        if self.load(account):
            return self.loaded[account]
            #then return account data
        pass
    def load(self,account):
        if not account in self.allowed:
            return False
        self.loaded[account] = load_file(f"account/l{account}.csv")
        return True
        
    def update(self, game):
        # length = len(word)
        # self.updated.add(length)
        # if length in self.loaded:
        #     self.loaded[length].append(word.lower())
        # else:
        #     self.loaded[length] = [word.lower()]
        pass
    def exit(self):
        # for length in self.updated:
        #     overwrite_file(f"words/l{length}.csv", self.loaded[length])
        pass