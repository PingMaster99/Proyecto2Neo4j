import csv
from neo4j import GraphDatabase
from py2neo import Graph, Node, Relationship, Database,NodeMatcher

#graph = Graph()
#driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "1234"), encrypted=False)
#db=Graph("http://neo4j:1234@127.0.0.1:7474/db/data")


#ESTE CUESTIONARIO LO AGREGAMOS AL FINAL

# uri=input("¡Es hora de iniciar! ¿Cual es su URI?\n")
# user=input("¿Cual es su usuario?\n")
# password=input("¿Cual es su password?\n")

db=Graph(uri="bolt://localhost:7687",user="neo4j",password="1234")

#we open the csv file and create a dictionary of key = character names and value = list with attributes
with open('smashCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    characterDict = {}
    for row in csv_reader:
        characterDict[row[0]] = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]

#we remove the header from the csv file
characterDict.pop("Name")

# here we create our database. we start with the the main connecting nodes

#fight style
brawler = Node("Style", name="Brawler")
swordfighter = Node("Style", name="Swordfighter")
gunner = Node("Style", name="Gunner")

#Up b out of shield
hasOOS=Node("OOS",name="Has_OOS")
noOOS=Node("OOS",name="No_OOS")

#weight
lightweight=Node("Weight",name="Lightweight")
mediumweight=Node("Weight",name="Mediumweight")
heavyweight=Node("Weight",name="Heavyweight")

#tier
stier=Node("Tier",name="S Tier")
atier=Node("Tier",name="A Tier")
btier=Node("Tier",name="B Tier")
ctier=Node("Tier",name="C Tier")
dtier=Node("Tier",name="D Tier")

#jumps
twoJumps=Node("Jumps",name="Two Jumps")
threeJumps=Node("Jumps",name="Three Jumps")
fourJumps=Node("Jumps",name="Four Jumps")
sixJumps=Node("Jumps",name="Six Jumps")

#sagas
starfox=Node("Saga",name="Starfox")
bayonetta=Node("Saga",name="Bayonetta")
supermariobros=Node("Saga",name="Super Mario Bros")
fzero=Node("Saga",name="F-Zero")
fireemblem=Node("Saga",name="Fire Emblem")
kidicarus=Node("Saga",name="Kid Icarus")
donkeykong=Node("Saga",name="Donkey Kong")
duckhunt=Node("Saga",name="Duck Hunt")
metroid=Node("Saga",name="Metroid")
zelda=Node("Saga",name="The Legend of Zelda")
pokemon=Node("Saga",name="Pokemon")
iceclimbers=Node("Saga",name="Ice Climbers")
splatoon=Node("Saga",name="Splatoon")
animalcrossing=Node("Saga",name="Animal Crossing")
streetfighter=Node("Saga",name="Street Fighter")
kingoffighters=Node("Saga",name="King of Fighters")
kirby=Node("Saga",name="Kirby")
punchout=Node("Saga",name="Punch-Out!")
megaman=Node("Saga",name="Mega Man")
gameandwatch=Node("Saga",name="Game and Watch")
earthbound=Node("Saga",name="Earthbound")
pikmin=Node("Saga",name="Pikmin")
nes=Node("Saga",name="N.E.S.")
castlevania=Node("Saga",name="Castlevania")
xenoblade=Node("Saga",name="Xenoblade Chronicles")
metalgearsolid=Node("Saga",name="Metal Gear Solid")
wiifit=Node("Saga",name="Wii Fit")
sonic=Node("Saga",name="Sonic")
dragonquest=Node("Saga",name="Dragon Quest")
persona=Node("Saga",name="Persona")
mii=Node("Saga",name="Mii")

#Type
human=Node("Type",name="Human")
fantasy=Node("Type",name="Fantasy")
animal=Node("Type",name="Animal")


#we create the main node relationships: brawler, swordfighter and gunner
bs = Relationship(brawler, "connectedTo", swordfighter)
db.create(bs)
sb = Relationship(swordfighter, "connectedTo", brawler)
db.create(sb)
bg = Relationship(brawler, "connectedTo", gunner)
db.create(bg)
gb = Relationship(gunner, "connectedTo", brawler)
db.create(gb)
sg = Relationship(gunner, "connectedTo", swordfighter)
db.create(sg)
gs = Relationship(swordfighter, "connectedTo", gunner)
db.create(gs)

#we need to know which category each character belongs to
for character in characterDict:
    if characterDict[character][1] == "Projectile":
        indicator="projectile"

    if characterDict[character][1] == "Brawler":
        indicator="brawler"

    if characterDict[character][1] == "Sword":
        indicator="swordfighter"

 
    oos=characterDict[character][2]
    weight=characterDict[character][3]
    tier=characterDict[character][4]
    jumps=characterDict[character][5]
    saga=characterDict[character][6]
    types=characterDict[character][7]
 

#we change the value of the dictionary key to a node of the character with its attributes
    characterDict[character] = Node("Character", name=characterDict[character][0], style=characterDict[character][1],
                                    oos=characterDict[character][2], weight=characterDict[character][3],
                                    tier=characterDict[character][4], jumps=characterDict[character][5],
                                    saga=characterDict[character][6], types=characterDict[character][7])
    
    #now we look for the match to put characters on their respective category: brawler, swordfighter, gunner
    if(indicator=="brawler"):
        a = Relationship(characterDict[character], "is", brawler)
        db.create(a)
    if(indicator=="swordfighter"):
        a = Relationship(characterDict[character], "is", swordfighter)
        db.create(a)
    if(indicator=="projectile"):
        a = Relationship(characterDict[character], "is", gunner)
        db.create(a)

#up b out of shield
    if(oos=="Yes"):
        a = Relationship(characterDict[character], "has_oos", hasOOS)
        db.create(a)
    if(oos=="No"):
        a = Relationship(characterDict[character], "has_oos", noOOS)
        db.create(a)

#weight
    if(weight=="Heavy"):
        a = Relationship(characterDict[character], "weight", heavyweight)
        db.create(a)
    if(weight=="Medium"):
        a = Relationship(characterDict[character], "weight", mediumweight)
        db.create(a)
    if(weight=="Light"):
        a = Relationship(characterDict[character], "weight", lightweight)
        db.create(a)

#tier
    if(tier=="A"):
        a = Relationship(characterDict[character], "tier", atier)
        db.create(a)
    if(tier=="S"):
        a = Relationship(characterDict[character], "tier", stier)
        db.create(a)
    if(tier=="B"):
        a = Relationship(characterDict[character], "tier", btier)
        db.create(a)
    if(tier=="C"):
        a = Relationship(characterDict[character], "tier", ctier)
        db.create(a)
    if(tier=="D"):
        a = Relationship(characterDict[character], "tier", dtier)
        db.create(a)

#jumps
    if(jumps=="2"):
        a = Relationship(characterDict[character], "jumps", twoJumps)
        db.create(a)
    if(jumps=="3"):
        a = Relationship(characterDict[character], "jumps", threeJumps)
        db.create(a)
    if(jumps=="4"):
        a = Relationship(characterDict[character], "jumps", fourJumps)
        db.create(a)
    if(jumps=="6"):
        a = Relationship(characterDict[character], "jumps", sixJumps)
        db.create(a)

#saga
    if(saga=="Star Fox"):
        a = Relationship(characterDict[character], "saga", starfox)
        db.create(a)
    if(saga=="Bayonetta"):
        a = Relationship(characterDict[character], "saga", bayonetta)
        db.create(a)
    if(saga=="Super Mario Bros"):
        a = Relationship(characterDict[character], "saga", supermariobros)
        db.create(a)
    if(saga=="F-Zero"):
        a = Relationship(characterDict[character], "saga", fzero)
        db.create(a)
    if(saga=="Fire Emblem"):
        a = Relationship(characterDict[character], "saga", fireemblem)
        db.create(a)
    if(saga=="Kid Icarus"):
        a = Relationship(characterDict[character], "saga", kidicarus)
        db.create(a)
    if(saga=="Donkey Kong"):
        a = Relationship(characterDict[character], "saga", donkeykong)
        db.create(a)
    if(saga=="Duck Hunt"):
        a = Relationship(characterDict[character], "saga", duckhunt)
        db.create(a)
    if(saga=="Metroid"):
        a = Relationship(characterDict[character], "saga", metroid)
        db.create(a)
    if(saga=="The Legend of Zelda"):
        a = Relationship(characterDict[character], "saga", zelda)
        db.create(a)
    if(saga=="Pokemon"):
        a = Relationship(characterDict[character], "saga", pokemon)
        db.create(a)
    if(saga=="Ice Climbers"):
        a = Relationship(characterDict[character], "saga", iceclimbers)
        db.create(a)
    if(saga=="Splatoon"):
        a = Relationship(characterDict[character], "saga", splatoon)
        db.create(a)
    if(saga=="Animal Crossing"):
        a = Relationship(characterDict[character], "saga", animalcrossing)
        db.create(a)
    if(saga=="Street Fighter"):
        a = Relationship(characterDict[character], "saga", streetfighter)
        db.create(a)
    if(saga=="King of Fighters"):
        a = Relationship(characterDict[character], "saga", kingoffighters)
        db.create(a)
    if(saga=="Kirby"):
        a = Relationship(characterDict[character], "saga", kirby)
        db.create(a)
    if(saga=="Punch-Out"):
        a = Relationship(characterDict[character], "saga", punchout)
        db.create(a)
    if(saga=="Mega Man"):
        a = Relationship(characterDict[character], "saga", megaman)
        db.create(a)
    if(saga=="Game & Watch"):
        a = Relationship(characterDict[character], "saga", gameandwatch)
        db.create(a)
    if(saga=="Earthbound"):
        a = Relationship(characterDict[character], "saga", earthbound)
        db.create(a)
    if(saga=="Pikmin"):
        a = Relationship(characterDict[character], "saga", pikmin)
        db.create(a)
    if(saga=="Xenoblade Chronicles"):
        a = Relationship(characterDict[character], "saga", xenoblade)
        db.create(a)
    if(saga=="Metal Gear Solid"):
        a = Relationship(characterDict[character], "saga", metalgearsolid)
        db.create(a)
    if(saga=="Wii Fit"):
        a = Relationship(characterDict[character], "saga", wiifit)
        db.create(a)
    if(saga=="Sonic"):
        a = Relationship(characterDict[character], "saga", sonic)
        db.create(a)
    if(saga=="Dragon Quest"):
        a = Relationship(characterDict[character], "saga", dragonquest)
        db.create(a)
    if(saga=="Persona"):
        a = Relationship(characterDict[character], "saga", persona)
        db.create(a)
    if(saga=="Mii"):
        a = Relationship(characterDict[character], "saga", mii)
        db.create(a)

    #we upload them to the database one by one  
    c=characterDict[character]
    db.create(c)
