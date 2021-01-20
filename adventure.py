#!/usr/bin/env python

# "Adventure" by Maxim Zmudzinski

import random, pickle#, curses
from dics import *
from time import sleep
from threading import Timer

class Building(): # Building class to store info on a building
    def __init__(self, type, location, shop):
        self.typeid = type
        self.location = location
        self.shop = shop
        self.uniqueid = location*100 + type # allows for custom dialog

def save(d, money, location, inventory, inside):
    savefile = open("saves/savefile.dat", "wb")
    pickle.dump(d, savefile)
    pickle.dump(money, savefile)
    pickle.dump(location, savefile)
    pickle.dump(inventory, savefile)
    pickle.dump(inside, savefile)
    savefile.close()
    print("Game saved.")

def buildingfunc(buildingclassobj):
    if buildingclassobj.shop == True: # Shops
        rdialog = regulardialog[buildingclassobj.typeid]
        print(rdialog)
        shopping = shopitems[buildingclassobj.typeid]
        print("Options:")
        if buildingclassobj.shop == 3:
            print("Note: Only the most powerful weapon will be used.")
        for sell in shopping:
            price = prices[buildingclassobj.typeid]
            print(items[sell]+", $"+str(price[sell]))
        item = None
        while item == None:
            cmd = input()
            number = 0
            for sell in shopping:
                number = number + 1
                global money
                if cmd == items[sell] or cmd == str(number) and money - price[sell] >= 0:
                    money = money - price[sell]
                    if sell == 17 or sell == 16:
                        if sell == 16:
                            vehicle = "bus"
                            item = 16
                            directions = busneighbors[buildingclassobj.location]
                        if sell == 17:
                            vehicle = "train"
                            item = 17
                            directions = trainneighbors[buildingclassobj.location]

                        print("What town would you like to move to by "+vehicle+"? (select either by spelling out the town name or writing what number in the list it is.)")
                        for locations in directions:
                            print(townnames[locations])
                        moved = False
                        while moved == False:
                            cmd = input()
                            number = 0
                            for locations in directions:
                                number = number+1
                                if cmd == townnames[locations] or cmd == str(number):
                                    location = locations
                                    inside = 14
                                    moved = True
                            if moved == False:
                                print("Not a town name. Please copy the name exactly or write the number it is in the list.")
                        print("Welcome to "+towndes[buildingclassobj.location])
                        item = True

                    elif sell == 15:
                        print("Nothing happens yet if you go to a inn.") # TODO: get rid of it and add cooking
                        item = True

                    else:
                        inventory.append(sell)
                        item = sell
                        print("You bought the "+items[sell]+".")

                elif cmd == items[sell] and money - price[sell] <= 0:
                    item = False
            if cmd == "cancel":
                print("Purchase cancelled.")
                item = -1
            if item == None:
                print("That is not an item. Please copy the name exactly.")
            elif item == False:
                print("You do not have enough money to afford that item.")

    if buildingclassobj.shop == False: # TODO: Jobs
        print("Jobs have not been implemented yet. Please come back later.")

    if buildingclassobj.shop == None: # Story dialog
        try:
            cdialog = customdialog[buildingclassobj.uniqueid]
            exists = True
        except:
            exists = False
        if exists == True:
            rdialog = regulardialog[buildingclassobj.typeid]
            cdialog.extend(rdialog)
            print(cdialog[random.randint(0, len(cdialog)-1)])
        else:
            rdialog = regulardialog[buildingclassobj.typeid]
            print(rdialog[random.randint(0, len(rdialog)-1)])

def youratk(inventory):
    highest = 0
    for item in inventory:
        if item in weapons:
            current = weapondmg[item]
            if current > highest:
                highest = current
    return highest

def ambush(d, inventory, money):
    chance = d * 10
    if random.randint(0, 100) <= chance:
        print("Bandits attack you on the way!") # TODO: Add some variation to the message.
        print("Do you fight, with a risk of dying and losing everything, or do you surrender to their demands and give them half your money?")
        winchance = fight(d, inventory)
        print("You take out your",)
        if random.randint(0, 100) <= winchance:
            return True
        else:
            return False

def fight(d, inventory):
    print(d)
    yatk = youratk(inventory)
    tatk = random.randint(1, d)
    dchance = 1.0 + ((d - 2.0) / 20.0)
    if dchance == 1.35:
        dchance = 1.8
    #                 Determines what chance you have to win
    #           1-10   1-4       balance    0-15              1 - 1.8
    winchance = ((yatk - tatk * 25) + (50)) / (dchance)
    print("You have a", winchance, "% chance of success.")
    sleep(1)
    print("You can increase this chance if you win the rock paper scissors tournament - (sword beats heal, heal beats shield, shield beats sword.)")
    sleep(3)
    print("However, instead of saying which you will do at the same time, you get to see the computer's answer first and you have 2 seconds to write the counter.")
    sleep(4)
    print("Good luck!")
    sleep(0.8)
    print("Starting in 3,")
    sleep(1)
    print("2,")
    sleep(1)
    print("1,")
    sleep(1)
    print("GO!")
    sleep(0.3)
    timescorrect = 0
    for round in [1,2,3]:
        opponentmove = random.choice(["sword", "heal", "shield"])
        optimalmove = bestmove[opponentmove]
        print("Opponent: "+opponentmove)
        timeout = 3.5
        threadtimer = Timer(timeout, ['Sorry, times up!'])
        threadtimer.start()
        answer = input("You: ")
        if answer == optimalmove:
            timescorrect == timescorrect + 1
        threadtimer.cancel()
        if round != 3:
            print("Next round:")
    winchance = winchance + 5 * timescorrect
    print("You have gained", 5 * timescorrect, "bonus points!")
    return winchance

def death():
    # Make sure that you lose your items too, along with your money
    # Also have the loading code be a function
    pass

# ---------------------------------------------------------------------- Loading code -----------------------------------------------------------------------------

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
    print("Choose a difficulty - Easy, Normal, Hard, or INSANE.")
    inside = None
    d = None
    while d == None:
        t = input()
        if t == "1" or t == "easy" or t == "Easy" or t == "e": # Easy mode config
            d = 2
            location = 1
            money = 50
        elif t == "2" or t == "normal" or t == "Normal" or t == "n": # Normal mode config
            d = 4
            location = 2
            money = 20
        elif t == "3" or t == "hard" or t == "Hard" or t == "h": # Hard mode config
            d = 6
            location = 3
            money = 10
        elif t == "4" or t == "insane" or t == "INSANE" or t == "i":
            d = 9
            location = 9
            money = 0
        else:
            print("Error, unable to interpert answer. Please try again.")

    # Some variable initiation
    inventory = [1]
    inside = 14
    save(d, money, location, inventory, inside)

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
    print("Welcome to "+towndes[location]) # Initial town message
    if money == 0:
        print("You are an aspiring adventurer, itching to get out of town. You only have the clothes on your back and a pocket knife to your name.")
    else:
        print("You are an aspiring adventurer, itching to get out of town. You only have "+str(money)+" dollars, the clothes on your back, and a pocket knife to your name.")

elif ifsave == True: # Loading save
    try:
        savefile = open("saves/savefile.dat", "rb")
        d = pickle.load(savefile)
        money = pickle.load(savefile)
        location = pickle.load(savefile)
        inventory = pickle.load(savefile)
        inside = pickle.load(savefile)
        savefile.close()
    except:
        print("Error - check that save file exists, or if it is incorrectly formatted.")
        exit()

# ------------------------------------------------------------------ Main code for commands -----------------------------------------------------------------------

print("Enter your commands below.")
while True: # All game commands
    cmd = input()
    if cmd == "move": # Moving from town to town
        print("What town would you like to move to? (select either by spelling out the town name or writing what number in the list it is.)")
        directions = neighbors[location]
        for locations in directions:
            print(townnames[locations])
        moved = False
        while moved == False:
            cmd = input()
            number = 0
            for locations in directions:
                number = number+1
                if cmd == townnames[locations] or cmd == str(number):
                    location = locations
                    inside = 14
                    moved = True
            if moved == False:
                print("Not a town name. Please copy the name exactly.")
        print("Welcome to "+towndes[location])
    elif cmd == "location": # Returns location
        print("You are in "+towndes[location])
        print("You are standing in the "+buildingdesc[inside])
    elif cmd == "exit" or cmd == "leave": # Stops the script
        print("Are you sure you want to leave the game? You will lose unsaved progress!")
        left = False
        while left == False:
            cmd = input()
            if cmd == "yes" or cmd == "Yes" or cmd == "Yes." or cmd == "YES" or cmd == "y" or cmd == "Y":
                left = True
                exit()
            elif cmd == "no" or cmd == "No" or cmd == "No." or cmd == "NO" or cmd == "n" or cmd == "N":
                left = None
                print("Leaving cancelled.")
            else:
                print("Error, unable to interpert answer. Please try again.")
    elif cmd == "save": # Saves game
        saved = False
        print("Are you sure you want to save? Any previous game will be overwritten!")
        while saved == False:
            cmd = input()
            if cmd == "yes" or cmd == "Yes" or cmd == "Yes." or cmd == "YES" or cmd == "y" or cmd == "Y":
                save(d, money, location, inventory, inside)
                saved = True
            elif cmd == "no" or cmd == "No" or cmd == "No." or cmd == "NO" or cmd == "n" or cmd == "N":
                print("Save cancelled.")
                saved = None
            else:
                print("Unable to interpert answer. Please try again.")

    elif cmd == "balance" or cmd == "bal": # Shows balance
        print("You have $"+str(money)+".")
    elif cmd == "beg": # gives money
        money = money + 10
        print("Someone gave you $10.")
    elif cmd == "pick": # gives a banana
        inventory.append(2)
        print("Ok you have picked a banana from... somewhere?")
    elif cmd == "inv" or cmd == "inventory" or cmd == "items": # displays inventory
        for item in inventory:
            print(items[item])
    elif cmd == "go" or cmd == "goto" or cmd == "visit":
        print("Which building would you like to visit? (Please copy the building name exactly or write the number in the list it is.)")
        buildings = townbuildings[location]
        for building in buildings:
            if building != 14:
                print(buildingtypes[building])
        moved = False
        while moved == False:
            cmd = input()
            number = 0
            for building in buildings:
                number = number + 1
                if cmd == buildingtypes[building] or cmd == str(number) and building != 14:
                    inside = building
                    moved = True
                    print("You have gone to the "+buildingdesc[building])
            if cmd == "cancel":
                moved = None
                print("Visit cancelled.")
            if moved == False:
                print("Not a building name. Please copy it exactly.")
    elif cmd == "search" or cmd == "look" or cmd == "chat" or cmd == "talk":
        if buildingfunctype[inside] == None and inside != 14:
            buildingis = Building(inside, location, buildingfunctype[inside])
            buildingfunc(buildingis)
        else:
            print("The building you are in does not let you chat.")
    elif cmd == "work":
        if buildingfunctype[inside] == False and inside != 14:
            buildingis = Building(inside, location, buildingfunctype[inside])
            buildingfunc(buildingis)
        else:
            print("The building you are in does not let you work.")
    elif cmd == "shop":
        if buildingfunctype[inside] == True and inside != 14:
            buildingis = Building(inside, location, buildingfunctype[inside])
            buildingfunc(buildingis)
        else:
            print("The building you are in does not let you shop.")
    elif cmd == "fighttest":
        fight(d, inventory)
    elif cmd == "help" or cmd == "commands" or cmd == "aaaaa" or cmd == "arghhhhhhh": # shows a list of what the commands do
        print("Commands: (note - subject to (constant) change)")
        print("'move'      - lets you move from one town to another.")
        print("'location'  - tells you your current location.")
        print("'visit'     - lets you move to a building.")
        print("'chat'      - lets you talk to NPCs if in a building that isnt a shop or a job.")
        print("'shop'      - opens the shop if it exists.")
        print("'save'      - saves your game.")
        print("'balance'   - tells you how much money you have.")
        print("'beg'       - gives you $10.")
        print("'pick'      - gives you a banana.")
        print("'inventory' - displays your inventory.")
    else:
        print("Not a command. (run 'help' for a list of commands)")
