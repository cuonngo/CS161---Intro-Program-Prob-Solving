# Copyright (c) 2011 Cuong Ngo
# Fishing Game

import random, pickle, shelve
class Fisher(object):
    """A New Fisher"""
    def __init__(self, name, score = 0):
        print("A new fisher has arrive!")
        self.name = name
        self.score = score
    def __str__(self):
        print("Your current scores is", player.score)
        rep = "\nAll scores:\n"
        rep += self.name + ": " + str(self.score) + "\n"
        return rep
    def talk(self):
        print("Hi. I'm", self.name, "my score is", player.score, "\n")
    def cast(self):
        global score
        fish = int(random.randint(1,100))
        if fish < 21:
            print("You caught Nothing!")
            print("It is worth 0 points.")
            player.score += 0
            print("Your current score is", player.score)
        elif 20 < fish < 41:
            print("You have caught a Minnow!")
            print("It is worth 10 points.")
            player.score += 10
            print("Your current score is", player.score)
        elif 40 < fish < 71:
            print("You have caught a Bluegill!")
            print("It is worth 30 points.")
            player.score += 30
            print("Your current score is", player.score)
        elif 70 < fish < 86:
            print("You have caught a Bass!")
            print("It is worth 100 points.")
            player.score += 100
            print("Your current score is", player.score)
        elif 85 < fish < 96:
            print("You have caught a Trout!")
            print("It is worth 200 points.")
            player.score += 200
            print("Your current score is", player.score)
        elif 95 < fish < 99:
            print("You have caught a Salmon!")
            print("It is worth 500 points.")
            player.score += 500
            print("Your current score is", player.score)
        elif fish == 100:
            print("You have caught a Gold Boot!")
            print("It is worth 5000 points.")
            player.score += 5000
            print("Your current score is", player.score)
        user_list[name] = player.score
def write():
    f = open("Fishing.dat", "wb")
    pickle.dump(user_list, f)
    f.close()
def read():
    f = open("fishinng.dat", "rb")
    user_list = pickle.load(f)
    print(user_list)    
user_list = {}
response = None
print("Fishing! Please enter fishing commands. \"help\" for help.")
try:
    read()
except:
    print("cannot load file")
while response != "quit":
    response = input(">")
    if response == "help":
        print(
        """
        Fishing Game

        register <username> - Register a new username
        fish <username> - Starts fishing as user <username>
        cast - Catch a fish
        scores - List the user's score, then all registered users scores
        quit - Quit game
        """
        )
    elif "register" in response:
        name = response[9:]        
        if "~" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "!" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "#" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "@" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "$" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "%" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "^" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "&" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "*" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "(" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif ")" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "+" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "=" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif ";" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif ":" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "]" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "[" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "}" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "{" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "'" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "<" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif ">" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "." in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "," in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "?" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif "|" in name:
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif name == "":
            print("Invalid name, name should only include letters, numbers, '_' and '-'")
        elif name in user_list:
            print("Name already exist! try another name")
        else:
            player = Fisher(name)
            player.talk()
            if name not in user_list:
                user_list[name] = player.score           
    elif response == "cast":
        player.cast()
    elif response == "scores":
        print("Your current scores is", player.score)
        print("\nAll scores:")
        for i in user_list:
            print(i + ":", user_list[i])
    elif "fish" in response:
        name = response[5:]
        if name in user_list:
            player.score = user_list[name]
        else:
            print("wrong name")
    elif response == "quit":
        print("Your current scores is", player.score)
        print("\nAll scores:")
        for i in user_list:
            print(i + ":", user_list[i])
        write()
    else:
        print("Not valid command. Please enter fishing comands. \"help\" for help.")
input("\n\nPress enter key to exit")
