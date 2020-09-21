import csv
from py2neo import Graph, Node, Relationship, NodeMatcher
"""
GenerateDatabase.py
------------------
Functions used to generate the database in Neo4j
------------------
Authors: 
    Isabel Ortiz        18176
    Douglas De León     18037
    Pablo Ruiz          18259
    
Taken from GenerateDatabase.py by: 
    Alejandro Álvarez   12429
    Joonho Kim          18096
    Pablo Ruiz          18259
    
Date: 
      21.09.2020
Version: 
      1.0.1
"""

"""
 IMPORTANT!!! If your neo4j conection has another localhost, user, or password,
 you need to change it in the next line of code for the program to work 
"""
db = Graph(uri="bolt://localhost:7687", user="neo4j", password="1234")

# Node matcher
matcher = NodeMatcher(db)


def generateDatabase():
    """Generates Neo4j database for Smash Bros. Main recommendation system
    Args:
        **
    Returns:
        **
    """
    # we open the csv file and create a dictionary of key = character names and value = list with attributes
    with open('smashCSV.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        characterDict = {}
        for row in csv_reader:
            characterDict[row[0]] = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]

    # we remove the header from the csv file
    characterDict.pop("Name")

    # we create the main node relationships: brawler, swordfighter and gunner
    db.create(Relationship(brawler, "connectedTo", swordfighter))
    db.create(Relationship(swordfighter, "connectedTo", brawler))
    db.create(Relationship(brawler, "connectedTo", gunner))
    db.create(Relationship(gunner, "connectedTo", brawler))
    db.create(Relationship(gunner, "connectedTo", swordfighter))
    db.create(Relationship(swordfighter, "connectedTo", gunner))

    # we need to know which category each character belongs to
    for character in characterDict:
        if characterDict[character][1] == "Projectile":
            indicator = "projectile"

        if characterDict[character][1] == "Brawler":
            indicator = "brawler"

        if characterDict[character][1] == "Sword":
            indicator = "swordfighter"

        oos = characterDict[character][2]
        weight = characterDict[character][3]
        tier = characterDict[character][4]
        jumps = characterDict[character][5]
        saga = characterDict[character][6]
        types = characterDict[character][7]

        # We change the value of the dictionary key to a node of the character with its attributes
        characterDict[character] = Node("Character", name=characterDict[character][0],
                                        style=characterDict[character][1],
                                        oos=characterDict[character][2], weight=characterDict[character][3],
                                        tier=characterDict[character][4], jumps=characterDict[character][5],
                                        saga=characterDict[character][6], types=characterDict[character][7])

        # now we look for the match to put characters on their respective category: brawler, swordfighter, gunner
        if indicator == "brawler":
            db.create(Relationship(characterDict[character], "is", brawler))
        elif indicator == "swordfighter":
            db.create(Relationship(characterDict[character], "is", swordfighter))
        elif indicator == "projectile":
            db.create(Relationship(characterDict[character], "is", gunner))

        # up b out of shield
        if oos == "Yes":
            db.create(Relationship(characterDict[character], "has_oos", hasOOS))
        elif oos == "No":
            db.create(Relationship(characterDict[character], "has_oos", noOOS))

        # weight
        if weight == "Heavy":
            db.create(Relationship(characterDict[character], "weight", heavyweight))
        elif weight == "Normal":
            db.create(Relationship(characterDict[character], "weight", mediumweight))
        elif weight == "Light":
            db.create(Relationship(characterDict[character], "weight", lightweight))

        # tier
        if tier == "A":
            db.create(Relationship(characterDict[character], "tier", atier))
        elif tier == "S":
            db.create(Relationship(characterDict[character], "tier", stier))
        elif tier == "B":
            db.create(Relationship(characterDict[character], "tier", btier))
        elif tier == "C":
            db.create(Relationship(characterDict[character], "tier", ctier))
        elif tier == "D":
            db.create(Relationship(characterDict[character], "tier", dtier))

        # jumps
        if jumps == "2":
            db.create(Relationship(characterDict[character], "jumps", twoJumps))
        elif jumps == "3":
            db.create(Relationship(characterDict[character], "jumps", threeJumps))
        elif jumps == "4":
            db.create(Relationship(characterDict[character], "jumps", fourJumps))
        elif jumps == "6":
            db.create(Relationship(characterDict[character], "jumps", sixJumps))

        # type
        if types == "Human":
            db.create(Relationship(characterDict[character], "type", human))
        elif types == "Fantasy":
            db.create(Relationship(characterDict[character], "type", fantasy))
        elif types == "Animal":
            db.create(Relationship(characterDict[character], "type", animal))

        # saga
        if saga == "Star Fox":
            db.create(Relationship(characterDict[character], "saga", starfox))
        elif saga == "Bayonetta":
            db.create(Relationship(characterDict[character], "saga", bayonetta))
        elif saga == "Super Mario Bros":
            db.create(Relationship(characterDict[character], "saga", supermariobros))
        elif saga == "F-Zero":
            db.create(Relationship(characterDict[character], "saga", fzero))
        elif saga == "Fire Emblem":
            db.create(Relationship(characterDict[character], "saga", fireemblem))
        elif saga == "Kid Icarus":
            db.create(Relationship(characterDict[character], "saga", kidicarus))
        elif saga == "Donkey Kong":
            db.create(Relationship(characterDict[character], "saga", donkeykong))
        elif saga == "Duck Hunt":
            db.create(Relationship(characterDict[character], "saga", duckhunt))
        elif saga == "Metroid":
            db.create(Relationship(characterDict[character], "saga", metroid))
        elif saga == "The Legend of Zelda":
            db.create(Relationship(characterDict[character], "saga", zelda))
        elif saga == "Pokemon":
            db.create(Relationship(characterDict[character], "saga", pokemon))
        elif saga == "Ice Climbers":
            db.create(Relationship(characterDict[character], "saga", iceclimbers))
        elif saga == "Splatoon":
            db.create(Relationship(characterDict[character], "saga", splatoon))
        elif saga == "Animal Crossing":
            db.create(Relationship(characterDict[character], "saga", animalcrossing))
        elif saga == "Street Fighter":
            db.create(Relationship(characterDict[character], "saga", streetfighter))
        elif saga == "King of Fighters":
            db.create(Relationship(characterDict[character], "saga", kingoffighters))
        elif saga == "Kirby":
            db.create(Relationship(characterDict[character], "saga", kirby))
        elif saga == "Punch-Out":
            db.create(Relationship(characterDict[character], "saga", punchout))
        elif saga == "Mega Man":
            db.create(Relationship(characterDict[character], "saga", megaman))
        elif saga == "Game & Watch":
            db.create(Relationship(characterDict[character], "saga", gameandwatch))
        elif saga == "Earthbound":
            db.create(Relationship(characterDict[character], "saga", earthbound))
        elif saga == "Pikmin":
            db.create(Relationship(characterDict[character], "saga", pikmin))
        elif saga == "NES":
            db.create(Relationship(characterDict[character], "saga", nes))
        elif saga == "Castlevania":
            db.create(Relationship(characterDict[character], "saga", castlevania))
        elif saga == "Xenoblade Chronicles":
            db.create(Relationship(characterDict[character], "saga", xenoblade))
        elif saga == "Metal Gear Solid":
            db.create(Relationship(characterDict[character], "saga", metalgearsolid))
        elif saga == "Wii Fit":
            db.create(Relationship(characterDict[character], "saga", wiifit))
        elif saga == "Sonic":
            db.create(Relationship(characterDict[character], "saga", sonic))
        elif saga == "Dragon Quest":
            db.create(Relationship(characterDict[character], "saga", dragonquest))
        elif saga == "Persona":
            db.create(Relationship(characterDict[character], "saga", persona))
        elif saga == "Mii":
            db.create(Relationship(characterDict[character], "saga", mii))

        # we upload them to the database one by one
        c = characterDict[character]
        db.create(c)


def generateUser(user_preferences: dict):
    """Generates the user in the database
    Args:
        *user_preferences (dict)
    Returns:
        **
    """
    user = Node("User", experience=user_preferences["experience"], style=user_preferences["fight_style"],
                weight=user_preferences["speed_and_weight"], oos=user_preferences["out_of_shield"],
                tier=user_preferences["tier"], jumps=user_preferences["jump"], saga=user_preferences["saga"],
                types=user_preferences["character_type"])
    db.create(user)

    # Fight style
    if user_preferences["fight_style"] == "Brawler":
        db.create(Relationship(user, "is", brawler))
    elif user_preferences["fight_style"] == "Sword":
        db.create(Relationship(user, "is", swordfighter))
    else:
        db.create(Relationship(user, "is", gunner))

    # Speed and weight
    if user_preferences["speed_and_weight"] == "Light":
        db.create(Relationship(user, "weight", lightweight))
    elif user_preferences["speed_and_weight"] == "Normal":
        db.create(Relationship(user, "weight", mediumweight))
    else:
        db.create(Relationship(user, "weight", heavyweight))

    # Out of shield attacks
    if user_preferences["out_of_shield"] == "Yes":
        db.create(Relationship(user, "has_oos", hasOOS))
    else:
        db.create(Relationship(user, "has_oos", noOOS))

    # User tier
    if user_preferences["tier"] == "S":
        db.create(Relationship(user, "tier", stier))
    elif user_preferences["tier"] == "A":
        db.create(Relationship(user, "tier", atier))
    elif user_preferences["tier"] == "B":
        db.create(Relationship(user, "tier", btier))
    elif user_preferences["tier"] == "C":
        db.create(Relationship(user, "tier", ctier))
    elif user_preferences["tier"] == "D":
        db.create(Relationship(user, "tier", dtier))
    else:
        db.create(Relationship(user, "tier", stier))
        db.create(Relationship(user, "tier", atier))
        db.create(Relationship(user, "tier", btier))
        db.create(Relationship(user, "tier", ctier))
        db.create(Relationship(user, "tier", dtier))

    # Preferred jumps
    if user_preferences["jump"] == "2":
        db.create(Relationship(user, "jumps", twoJumps))
    elif user_preferences["jump"] == "3":
        db.create(Relationship(user, "jumps", threeJumps))
    elif user_preferences["jump"] == "4":
        db.create(Relationship(user, "jumps", fourJumps))
    elif user_preferences["jump"] == "6":
        db.create(Relationship(user, "jumps", sixJumps))

    # Saga
    saga = user_preferences["saga"]
    if saga == "Star Fox":
        db.create(Relationship(user, "saga", starfox))
    elif saga == "Bayonetta":
        db.create(Relationship(user, "saga", bayonetta))
    elif saga == "Super Mario Bros":
        db.create(Relationship(user, "saga", supermariobros))
    elif saga == "F-Zero":
        db.create(Relationship(user, "saga", fzero))
    elif saga == "Fire Emblem":
        db.create(Relationship(user, "saga", fireemblem))
    elif saga == "Kid Icarus":
        db.create(Relationship(user, "saga", kidicarus))
    elif saga == "Donkey Kong":
        db.create(Relationship(user, "saga", donkeykong))
    elif saga == "Duck Hunt":
        db.create(Relationship(user, "saga", duckhunt))
    elif saga == "Metroid":
        db.create(Relationship(user, "saga", metroid))
    elif saga == "The Legend of Zelda":
        db.create(Relationship(user, "saga", zelda))
    elif saga == "Pokemon":
        db.create(Relationship(user, "saga", pokemon))
    elif saga == "Ice Climbers":
        db.create(Relationship(user, "saga", iceclimbers))
    elif saga == "Splatoon":
        db.create(Relationship(user, "saga", splatoon))
    elif saga == "Animal Crossing":
        db.create(Relationship(user, "saga", animalcrossing))
    elif saga == "Street Fighter":
        db.create(Relationship(user, "saga", streetfighter))
    elif saga == "King of Fighters":
        db.create(Relationship(user, "saga", kingoffighters))
    elif saga == "Kirby":
        db.create(Relationship(user, "saga", kirby))
    elif saga == "Punch-Out":
        db.create(Relationship(user, "saga", punchout))
    elif saga == "Mega Man":
        db.create(Relationship(user, "saga", megaman))
    elif saga == "Game & Watch":
        db.create(Relationship(user, "saga", gameandwatch))
    elif saga == "Earthbound":
        db.create(Relationship(user, "saga", earthbound))
    elif saga == "Pikmin":
        db.create(Relationship(user, "saga", pikmin))
    elif saga == "NES":
        db.create(Relationship(user, "saga", nes))
    elif saga == "Castlevania":
        db.create(Relationship(user, "saga", castlevania))
    elif saga == "Xenoblade Chronicles":
        db.create(Relationship(user, "saga", xenoblade))
    elif saga == "Metal Gear Solid":
        db.create(Relationship(user, "saga", metalgearsolid))
    elif saga == "Wii Fit":
        db.create(Relationship(user, "saga", wiifit))
    elif saga == "Sonic":
        db.create(Relationship(user, "saga", sonic))
    elif saga == "Dragon Quest":
        db.create(Relationship(user, "saga", dragonquest))
    elif saga == "Persona":
        db.create(Relationship(user, "saga", persona))
    elif saga == "Mii":
        db.create(Relationship(user, "saga", mii))


def delete():
    """ Deletes everything from the database
    Args:
        **
    Returns:
        **
    """
    db.delete_all()

# Connecting nodes for the database


# fight style
brawler = Node("Style", name="Brawler")
swordfighter = Node("Style", name="Swordfighter")
gunner = Node("Style", name="Gunner")

# Up b out of shield
hasOOS = Node("OOS", name="Has_OOS")
noOOS = Node("OOS", name="No_OOS")

# weight
lightweight = Node("Weight", name="Lightweight")
mediumweight = Node("Weight", name="Mediumweight")
heavyweight = Node("Weight", name="Heavyweight")

# tier
stier = Node("Tier", name="S Tier")
atier = Node("Tier", name="A Tier")
btier = Node("Tier", name="B Tier")
ctier = Node("Tier", name="C Tier")
dtier = Node("Tier", name="D Tier")

# jumps
twoJumps = Node("Jumps", name="Two Jumps")
threeJumps = Node("Jumps", name="Three Jumps")
fourJumps = Node("Jumps", name="Four Jumps")
sixJumps = Node("Jumps", name="Six Jumps")

# sagas
starfox = Node("Saga", name="Starfox")
bayonetta = Node("Saga", name="Bayonetta")
supermariobros = Node("Saga", name="Super Mario Bros")
fzero = Node("Saga", name="F-Zero")
fireemblem = Node("Saga", name="Fire Emblem")
kidicarus = Node("Saga", name="Kid Icarus")
donkeykong = Node("Saga", name="Donkey Kong")
duckhunt = Node("Saga", name="Duck Hunt")
metroid = Node("Saga", name="Metroid")
zelda = Node("Saga", name="The Legend of Zelda")
pokemon = Node("Saga", name="Pokemon")
iceclimbers = Node("Saga", name="Ice Climbers")
splatoon = Node("Saga", name="Splatoon")
animalcrossing = Node("Saga", name="Animal Crossing")
streetfighter = Node("Saga", name="Street Fighter")
kingoffighters = Node("Saga", name="King of Fighters")
kirby = Node("Saga", name="Kirby")
punchout = Node("Saga", name="Punch-Out!")
megaman = Node("Saga", name="Mega Man")
gameandwatch = Node("Saga", name="Game and Watch")
earthbound = Node("Saga", name="Earthbound")
pikmin = Node("Saga", name="Pikmin")
nes = Node("Saga", name="N.E.S.")
castlevania = Node("Saga", name="Castlevania")
xenoblade = Node("Saga", name="Xenoblade Chronicles")
metalgearsolid = Node("Saga", name="Metal Gear Solid")
wiifit = Node("Saga", name="Wii Fit")
sonic = Node("Saga", name="Sonic")
dragonquest = Node("Saga", name="Dragon Quest")
persona = Node("Saga", name="Persona")
mii = Node("Saga", name="Mii")

# Type
human = Node("Type", name="Human")
fantasy = Node("Type", name="Fantasy")
animal = Node("Type", name="Animal")
