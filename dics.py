towndes = { # To reference town names
    1: "Halifax, a metropolis with many thriving industries, giving it a lot of power over the surrounding areas.",
    2: "Sydney, a city with a lot of emphasis on its industrial sectors.",
    3: "Sandford, a village with fishing as the main revenue source.",
    4: "Clark's Harbor, a village with lobster fishing being the livelihood of most of the people there.",
    5: "Lunenburg, a town with a huge fish processing industry.",
    6: "Wolfville, a bustling town with a thriving tourist industry, with the wine industry and the history being large attractions.",
    7: "Annapolis Royal, a village with a strong tourist, ship renovation and scallop industry.",
    8: "Truro, a large, historic town which serves as an gateway to the outside world.",
    9: "Port Dufferin, a tiny village with very little industry.",
    10: "New Glasgow, a city with a fairly big manufacturing industry, along with the corporate headquarters of Savy's.",
    11: "Port Hawkesbury, a town with a big shipping industry, along with a large paper manufacturing industry.",
    12: "Inverness, a small town that once had a small coal mining industry, but now has a tourisim industry based on two popular golf courses.",
    13: "Dingwall, a village that has a small fishing industry, along with a minor tourist industry.",
}
townbuildings = { # What buildings there are in each town
    1: [1, 2, 3, 4, 5, 6, 9, 13, 14, 15],
    2: [1, 2, 3, 5, 6, 8, 9, 10, 14],
    3: [1, 2, 8, 14],
    4: [4, 6, 8, 9, 14],
    5: [1, 2, 4, 8, 11, 14],
    6: [1, 2, 4, 13, 14, 15],
    7: [1, 2, 3, 4, 8, 9, 14, 15],
    8: [1, 2, 5, 6, 9, 13, 14, 15],
    9: [8, 14],
    10: [1, 2, 5, 6, 9, 10, 14, 16],
    11: [1, 2, 3, 5, 9, 10, 14],
    12: [2, 7, 8, 12, 13, 14],
    13: [2, 8, 14, 15],
}
regulardialog = {
    1: ["Cashier: Welcome to Savy's! What would you like to purchase today?", "Cashier: What's going on! What would you like to purchase today?"],
    2: ["Associate: What's going on! Need a guide? Well lemme call one up.", "Associate: Morning! My, you wake up early! Well, we can probably find a guide that is awake."],
    3: ["Blacksmith: Welcome to Metalworking Inc. Our tools are right some good, I find!", "Blacksmith: What's going on! We sell a mulitude of right some good weapons for the aspiring adventurer such as yourself!"],
    4: ["Ticket Machine: Please insert $30 into the ticket machine."],
    5: ["Ticket Machine: Please insert $15 into the ticket machine."],
    6: ["Receptionist: Welcome to the local branch of the Nova Scotian Provincial Government.", "Politictian: I hate politics. It's so borringg. But my bribes pay wel- I MEAN the government... yes.", "Someone's Uncle: Back in my day, we would just go out and bomb 'em!\nPolitictian: Have you been reading the alernate reality books again? Sigh.", "Politictian: Sometimes the things that get passed are so ridiculous, I almost think the world is a videogame or something. Ridiculous, right?"],
    12: ["You look inside of the cave - it's all dark and dusty, making you expect a monster to jump out at any moment, like in those old horror movies."],
    13: ["Bartenter: Want a drink? Just dont drink so much you get paralyzed!"],
    14: ["This game was made by Maxim Zmudzinski. Also, you could only be reading the code to find this (;"],
    15: ["You look around, and see many fairly rich looking people staring at paintings on walls. Looks boring.", "Art Admirer: Wow. C. Monet really outdid himself with this one!", "Kid: I wanna go home, this is boooorrring.\nMother: But look at the paintings! Aren't they beautiful?", "Tourist: Hey Jenna, wanna take a selfie with this one?", "'Jenna': Selfie time!",],
}
customdialog = {
    106: ["Politictian: I can't belive they actually passed that bill. It's a disgrace to all uf us!", "Politictian: Finally! They passed the bill!"],
    406: ["Politictian: Sometimes I wonder why on Earth they built a Government branch here. This place is in the middle of nowhere!", "Politictian: I better get back to fishing. I need lunch, right? I guess could just buy it from - what was it, Savy's?"],
    815: ["Mueseum Director: We was very busy an hour ago - I think there was an after-party group.", "Partygoer: This mueseum is boring - I should've left with the others."],
}
buildingtypes = { # To reference building types
    1: "Savy's General Store", # Shop
    2: "Trail Guide Association", # Shop
    3: "Metalworking Inc.", # Shop
    4: "Bus Stop", # Shop
    5: "Train Station", # Shop
    6: "Government Building", # Story
    7: "Golf Course", # Job
    8: "Fishery", # Job
    9: "Port", # Job
    10: "Factory", # Job
    11: "Fish Processing Plant", # Job
    12: "Old Coal Mine", # Story
    13: "Bar", # Shop
    14: "Town Square", # Default
    15: "Mueseum", # Story
    16: "Savy's Headquarters", # Job
}
buildingfunctype = { # What type of function each building should have - True is shop, False is job, None is story (dialog)
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: None,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: None,
    13: True,
    14: None,
    15: None,
    16: False,
}
buildingdesc = { # To reference building descriptions
    1: "Savy's General Store, a multiprovincial grocery chain.",
    2: "Bed & Breakfast Inn, a local inn owned by a local guy.",
    3: "Metalworking Inc., a cross-provicial metalworking company.",
    4: "Bus Stop",
    5: "Train Station",
    6: "Government Building",
    7: "Golf Course, which is filled with tourist golfers.",
    8: "Fishery, where you see a 'hiring' flyer posted.",
    9: "Port, which has many ships moving in and out regularly. You notice a 'work needed' sign as well.",
    10: "Factory. There are tons of people working, but they can't seem to get the job done fast enough. Perhaps they need a hand?",
    11: "Fish Processing Plant, where a bunch of people that look like sushi chefs are chopping fish.",
    12: "Old Coal Mine, which looks like a huge, dark hole in the ground with rusty elevators leading down.",
    13: "Bar, which is filled with people having a drink after a long day at work.",
    14: "Town Square.",
    15: "Mueseum, which has a sparse distribution of people looking at various paintings and sculptures.",
    16: "Savy's Headquarters. You look up at the cold building and shiver with intimidation. They seem to be hiring though.",
}
townnames = { # To reference town names
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
townids = { # To reference town ids
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
trainneighbors = { # Which towns are next to which, train edition
    1: [8],
    8: [1, 10],
    10: [8, 11],
    11: [10, 2],
    2: [11],
}
busneighbors = { # Which towns are next to which, bus edition
    7: [6],
    6: [7, 1],
    1: [6, 5],
    5: [1, 4],
    4: [5],
}
items = { # To reference what the names of the items are
    1: "Pocket Knife",
    2: "Banana",
    3: "Savy Soda",
    4: "Butter",
    5: "White Bread",
    6: "Lake Whitefish",
    7: "Plain Rice",
    8: "Bottled Water",
    9: "Dry Spagetti",
    10: "Tomato Sauce",
    11: "Cereal",
    12: "Cow Milk",
    13: "Eggs",
    14: "Spices",
    15: "A night at the Inn",
    16: "Bus Ticket",
    17: "Train Ticket",
    18: "Dagger",
    19: "Iron Shortsword",
    20: "Iron Longsword",
    21: "Machete",
    22: "Pistol",
    23: "Rifle",
    24: "Shotgun",
    25: "Savy Beer",
    26: "White Wine",
    27: "Red Wine",
    28: "Cocktail",
    29: "Caesar Salad",
}
weapondmg = {
    1: 1,
    18: 2,
    19: 3,
    20: 4,
    21: 5,
    22: 6,
    23: 7,
    24: 8,
}
weapons = [18, 19, 20, 21, 22, 23, 24]
shopitems = { # To reference what each shop is selling
    1: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    2: [15],
    3: [18, 19, 20, 21, 22, 23, 24],
    4: [16],
    5: [17],
    13: [25, 26, 27, 28, 29],
}
prices = {
    1: {2: 5, 3: 2, 4: 8, 5: 10, 6: 10, 7: 15, 8: 10, 9: 5, 10: 8, 11: 12, 12: 10, 13: 12, 14: 5},
    2: {15: 20},
    3: {18: 20, 19: 50, 20: 100, 21: 200, 22: 300, 23: 500, 24: 1000},
    4: {16: 30},
    5: {17: 15},
    13: {25: 10, 26: 20, 27: 20, 28: 30, 29: 15},
}
bestmove = {
    "sword": "shield",
    "heal": "sword",
    "shield": "heal",
}
