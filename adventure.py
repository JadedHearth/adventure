# By Maxim Zmudzinski

import random
from time import sleep

class Building(object):
    def __init__(self, type, shop):
        self.type = type
        self.shop = shop

# some converting functions
def strtolst(string):
    instr = list(string.split(" "))
    return instr

def lsttostr(list):
    inlist = ' '.join([str(entry) for entry in list])
    return inlist

towndes = { # To reference town names
    1: "Halifax, a metropolis with many thriving industries, giving it a lot of power over the surrounding areas.",
    2: "Sydney, a city with a lot of emphasis on its industrial sectors.",
    3: "Sandford, a village with fishing as the main revenue source.",
    4: "Clark's Harbor, a village with lobster fishing being the livelihood of most of the people there.",
    5: "Lunenburg, a town with a huge fish processing industry.",
    6: "Wolfville, a bustling town with a thriving tourist industry, with the wine industry and the history being large attractions.",
    7: "Annapolis Royal, a village with a strong tourist, ship renovation and scallop industry.",
    8: "Truro, a large historic town which is an gateway to the outside world.",
    9: "Port Dufferin, a tiny village with very little industry.",
    10: "New Glasgow, a city with a fairly big manufacturing industry, along with the corporate headquarters of Savy's.",
    11: "Port Hawkesbury, a town with a big shipping industry, along with a large paper manufacturing industry.",
    12: "Inverness, a small town that once had a small coal mining industry, but now has a tourisim industry based on two popular golf courses.",
    13: "Dingwall, a village that has a small fishing industry, along with a minor tourist industry.",
}
townbuildings = { # What buildings there are in each town
    1: [1, 2, 3, 4, 5, 6, 9, 13, 14, 15],
    2: [1, 2, 3, 5, 8, 9, 10, 14],
    3: [2, 8, 14],
    4: [4, 8, 9, 14],
    5: [1, 2, 4, 8, 11],
    6: [1, 2, 4, 13, 14, 15],
    7: [1, 2, 3, 4, 8, 9, 14, 15],
    8: [1, 2, 5, 6, 9, 13, 15],
    9: [8, 14],
    10: [1, 2, 5, 6, 9, 10, 16],
    11: [1, 2, 3, 5, 9, 10],
    12: [1, 2, 7, 8, 12, 13],
    13: [2, 8, 15],
}
buildingtypes = { # To reference building types
    1: "Savy's General Store", # Shop
    2: "Inn", # Service
    3: "Blacksmith", # Shop
    4: "Bus Stop", # Service
    5: "Train Station", # Service
    6: "Government Buildings",
    7: "Golf Course", # Service
    8: "Fishery", # Shop
    9: "Port", # Service
    10: "Factory", # Service
    11: "Fish Processing Plant.", # Service
    12: "Old Coal Mine",
    13: "Bar", # Shop
    14: "Town Square",
    15: "Mueseum",
    16: "Savy's Headquarters"
}
townids = { # To reference town names
    1: "Halifax",
    2: "Sydney",
    3: "Sandford",
    4: "Clark's Harbor",
    5: "Lunenburg",
    6: "Wolfville",
    7: "Annapolis Royal",
    8: "Truro",
    9: "Port Dufferin",
    10: "New Glasgow",
    11: "Port Hawkesbury",
    12: "Inverness",
    13: "Dingwall",
}
townnames = { # To reference town names
    "Halifax": 1,
    "Sydney": 2,
    "Sandford": 3,
    "Clark's Harbor": 4,
    "Lunenburg": 5,
    "Wolfville": 6,
    "Annapolis Royal": 7,
    "Truro": 8,
    "Port Dufferin": 9,
    "New Glasgow": 10,
    "Port Hawkesbury": 11,
    "Inverness": 12,
    "Dingwall": 13,
}
neighbors = { # Reference to what towns are next to which
    1: [5, 6, 8, 9],
    2: [11, 13],
    3: [4, 7],
    4: [3, 5],
    5: [1, 4],
    6: [1, 7],
    7: [3, 6],
    8: [1, 10],
    9: [1, 11],
    10: [8, 11],
    11: [2, 9, 10, 12],
    12: [11, 13],
    13: [2, 12],
}
items = {
    1: "Dagger",
    2: "Banana",
}

print("\nWelcome to 'Adventure' by Maxim Zmudzinski.") # TODO: Extend description?

print("Would you like to load a save file?")
ifsave = None
while ifsave == None:
    cmd = input()
    if cmd == "yes" or cmd == "Yes" or cmd == "Yes." or cmd == "YES" or cmd == "y" or cmd == "Y":
        ifsave = True
    elif cmd == "no" or cmd == "No" or cmd == "No." or cmd == "NO" or cmd == "n" or cmd == "N":
        ifsave = False
    else:
        print("Error, unable to interpert answer. Please try again.")


if ifsave == False: # Creating a new game
    print("Creating new game...")
    print("Choose a difficulty - Easy, Normal, or Hard.")
    inside = None
    tmess = None
    while tmess == None:
        t = input()
        if t == "1" or t == "easy" or t == "Easy" or t == "e": # Easy mode config
            tmess = towndes[1]
            d = 1
            money = 60
        elif t == "2" or t == "normal" or t == "Normal" or t == "n": # Normal mode config
            tmess = towndes[2]
            d = 2
            money = 40
        elif t == "3" or t == "hard" or t == "Hard" or t == "h": # Hard mode config
            tmess = towndes[3]
            d = 3
            money = 20
        else:
            print("Error, unable to interpert answer. Please try again.")
    location = d
    inventory = [1]

    print("Would you like to do the tutorial?") # Tutorial query
    tut = None
    while tut != True and tut != False:
        tut = input()
        if tut == "yes" or tut == "Yes" or tut == "Yes." or tut == "YES" or tut == "y" or tut == "Y":
            tut = True
        elif tut == "no" or tut == "No" or tut == "No." or tut == "NO" or tut == "n" or tut == "N":
            tut = False
        else:
            print("Error, unable to interpert answer. Please try again.")
    if tut == True:
        print("havent done this yet") # TODO: interactive tutorial?
    print("Welcome to "+tmess) # Initial town message
    print("You are an aspiring adventurer, itching to get out of town. You only have "+str(money)+" dollars, the clothes on your back, and a dagger to your name.")


elif ifsave == True: # Loading save
    try:
        savefile = open("saves/savefile.txt", "r")
        d = int(savefile.readline())
        money = int(savefile.readline())
        location = int(savefile.readline())
        inventory = strtolst(savefile.readline())
        savefile.close()
    except:
        print("Error - check that save file exists, or if it is incorrectly formatted.")
        exit()

print("Enter your commands below.")
while True: # All game commands
    cmd = input()
    if cmd == "move": # Moving from town to town
        print("What town would you like to move to? (Please copy the town name exactly)")
        directions = neighbors[location]
        for locations in directions:
            print(townids[locations])
        moved = None
        while moved == None:
            cmd = input()
            for locations in directions:
                if cmd == townids[locations]:
                    location = townnames[cmd]
                    moved = True
            if moved == None:
                print("Not a town name. Please copy the name exactly.")
        print("Welcome to "+towndes[location])
    if cmd == "location": # Returns location
        print("You are in "+towndes[location])
    if cmd == "exit" or cmd == "leave": # Stops the script
        print("Are you sure you want to leave the game? You will lose all your unsaved progress!")
        left = None
        while left == None:
            cmd = input()
            if cmd == "yes" or cmd == "Yes" or cmd == "Yes." or cmd == "YES" or cmd == "y" or cmd == "Y":
                left = True
                exit()
            elif cmd == "no" or cmd == "No" or cmd == "No." or cmd == "NO" or cmd == "n" or cmd == "N":
                left = False
            else:
                print("Error, unable to interpert answer. Please try again.")
    if cmd == "save": # Saves game
        saved = None
        print("Are you sure you want to save? Any previous game will be overwritten!")
        while saved == None:
            cmd = input()
            if cmd == "yes" or cmd == "Yes" or cmd == "Yes." or cmd == "YES" or cmd == "y" or cmd == "Y":
                savefile = open("saves/savefile.txt", "w")
                savefile.write(str(d)+"\n"+str(money)+"\n"+str(location)+"\n"+lsttostr(inventory))
                savefile.close()
                print("Game saved.")
                saved = True
            elif cmd == "no" or cmd == "No" or cmd == "No." or cmd == "NO" or cmd == "n" or cmd == "N":
                print("Save cancelled.")
                saved = False
            else:
                print("Unable to interpert answer. Please try again.")

    if cmd == "balance" or cmd == "bal": # Shows balance
        print("You have $"+str(money)+".")
    if cmd == "beg": # gives money
        money = money + 10
        print("Someone gave you $10.")
    if cmd == "pick": # gives a banana
        inventory.append(2)
        print("Ok you have picked a banana from... somewhere?")
    if cmd == "inv" or cmd == "inventory" or cmd == "items": # displays inventory
        for item in inventory:
            print(items[item])
    if cmd == "help" or cmd == "aaaaaa" or cmd == "arghhhhhhh": # shows a list of what the commands do
        print("Commands: (note - subject to change)")
        print("'move'     - lets you move from one town to another.")
        print("'location' - tells you your current location.")
        print("'save'     - saves your game.")
        print("'balance'  - tells you how much money you have.")
        print("'beg'      - gives you $10.")
        print("'pick'     - gives you a banana.")
        print("'inventory'- displays your inventory.")
