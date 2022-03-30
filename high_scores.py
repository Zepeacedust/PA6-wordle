import glob
def load_file(filename):
    with open(filename, "r") as file:
        return file.read().split(",")
def get_valid_files():
    #finna öll leyfð files í words
    allowed = set()
    for file in glob.glob("accounts/a*.csv"):
        try:
            allowed.add(int(file[7:][:-4]))
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
        # assert isinstance(length, int)
        # #if length has been loaded before
        # if length in self.loaded:
        #     #return random word with given length
        #     return random.choice(self.loaded[length])
        # #else try to load it
        # if self.load(length):
        #     return random.choice(self.loaded[length])
        #     #then return random word with given length
        pass
    def load(self,account):
        # if not length in self.allowed:
        #     print("No words of that length exist, please try another")
        #     return False
        # print(f"Loading words of length {length}.")
        # self.loaded[length] = load_file(f"words/l{length}.csv")
        # return True
        pass
        
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