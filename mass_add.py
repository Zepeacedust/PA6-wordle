import loading_module

manager = loading_module.Word_Manager()
input_filename = input("enter .csv file name to process: ")
with open(input_filename,"r") as file:
    for word in file.read().split(","):
        manager.update(word.strip())
manager.exit()