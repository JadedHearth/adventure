#!/usr/bin/env python

# "adventure", a game made by Maxim Zmudzinski

import random, pickle
from dics import *
from time import sleep

class Building(): # Building class to store info on a building
    def __init__(self, type, location, shop):
        self.typeid = type
        self.location = location
        self.shop = shop
        self.uniqueid = location*100 + type # allows for custom dialog

def buildingfunc(buildingclassobj):
    if buildingclassobj.shop == True: # Shops
        global money
        rdialog = regulardialog[buildingclassobj.typeid]
        print(rdialog)
        shopping = shopitems[buildingclassobj.typeid]
        print("Options:")
        for sell in shopping:
            price = prices[buildingclassobj.typeid]
            print(items[sell]+", $"+str(price[sell]))
        item = None
        while item == None:
            cmd = input()
            for sell in shopping:
                if cmd == items[sell] and money - price[sell] >= 0:
                    money = money - price[sell]
                    inventory.append(sell)
                    item = True
                elif cmd == items[sell] and money - price[sell] <= 0:
                    item = False
            if cmd == "cancel":
                print("Purchase cancelled.")
                item = -1
            if item == None:
                print("That is not an item. Please copy the name exactly.")
            elif: item == False:
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
            print(cdialog[random.randint(0, len(cdialog)-1)])
        else:
            rdialog = regulardialog[buildingclassobj.typeid]
            print(rdialog)

#           Beginning of main code
#                      |
#                      |
#                      V

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
    print("Choose a difficulty - Easy, Normal, Hard, or EXTREME.")
    inside = None
    d = None
    while d == None:
        t = input()
        if t == "1" or t == "easy" or t == "Easy" or t == "e": # Easy mode config
            d = 1
            money = 50
        elif t == "2" or t == "normal" or t == "Normal" or t == "n": # Normal mode config
            d = 2
            money = 20
        elif t == "3" or t == "hard" or t == "Hard" or t == "h": # Hard mode config
            d = 3
            money = 10
        elif t == "4" or t == "extreme" or t == "EXTREME" or t == "e":
            d = 9
            money = 0
        else:
            print("Error, unable to interpert answer. Please try again.")

    # Some variable initiation
    location = d
    inventory = [1]
    inside = 14

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
    print("Welcome to "+towndes[d]) # Initial town message
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

print("Enter your commands below.")
while True: # All game commands
    cmd = input()
    if cmd == "move": # Moving from town to town
        print("What town would you like to move to? (Please copy the town name exactly)")
        directions = neighbors[location]
        for locations in directions:
            print(townids[locations])
        moved = False
        while moved == False:
            cmd = input()
            for locations in directions:
                if cmd == townids[locations]:
                    location = townnames[cmd]
                    inside = 14
                    moved = True
            if moved == False:
                print("Not a town name. Please copy the name exactly.")
        print("Welcome to "+towndes[location])
    if cmd == "location": # Returns location
        print("You are in "+towndes[location])
        print("You are standing in the "+buildingdesc[inside])
    if cmd == "exit" or cmd == "leave": # Stops the script
        print("Are you sure you want to leave the game? You will lose all your unsaved progress!")
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
    if cmd == "save": # Saves game
        saved = False
        print("Are you sure you want to save? Any previous game will be overwritten!")
        while saved == False:
            cmd = input()
            if cmd == "yes" or cmd == "Yes" or cmd == "Yes." or cmd == "YES" or cmd == "y" or cmd == "Y":
                savefile = open("saves/savefile.dat", "wb")
                pickle.dump(d, savefile)
                pickle.dump(money, savefile)
                pickle.dump(location, savefile)
                pickle.dump(inventory, savefile)
                pickle.dump(inside, savefile)
                savefile.close()
                print("Game saved.")
                saved = True
            elif cmd == "no" or cmd == "No" or cmd == "No." or cmd == "NO" or cmd == "n" or cmd == "N":
                print("Save cancelled.")
                saved = None
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
    if cmd == "go" or cmd == "goto" or cmd == "visit":
        print("Which building would you like to visit? (Please copy the town name exactly.)")
        buildings = townbuildings[location]
        for building in buildings:
            if building != 14:
                print(buildingtypes[building])
        moved = False
        while moved == False:
            cmd = input()
            for building in buildings:
                if cmd == buildingtypes[building] and building != 14:
                    inside = building
                    moved = True
                    print("You have gone to the "+buildingtypes[building]+".")
            if moved == False:
                print("Not a building name. Please copy it exactly.")
    if cmd == "search" or cmd == "look" or cmd == "chat" or cmd == "talk":
        if buildingfunctype[inside] == None:
            buildingis = Building(inside, location, buildingfunctype[inside])
            buildingfunc(buildingis)
        else:
            print("The building you are in does not let you chat.")
    if cmd == "work":
        buildingis = Building(inside, location, buildingfunctype[inside])
        buildingfunc(buildingis)
    if cmd == "shop":
        buildingis = Building(inside, location, buildingfunctype[inside])
        buildingfunc(buildingis)
    if cmd == "help" or cmd == "aaaaa" or cmd == "arghhhhhhh": # shows a list of what the commands do
        print("Commands: (note - subject to (constant) change)")
        print("'move'      - lets you move from one town to another.")
        print("'location'  - tells you your current location.")
        print("'visit'     - lets you move to a building")
        print("'chat'      - lets you talk to NPCs if in a building that isnt a shop or a job.")
        print("'shop'      - opens the shop if it exists")
        print("'save'      - saves your game.")
        print("'balance'   - tells you how much money you have.")
        print("'beg'       - gives you $10.")
        print("'pick'      - gives you a banana.")
        print("'inventory' - displays your inventory.")
