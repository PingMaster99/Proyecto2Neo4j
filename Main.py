import csv
from neo4j import GraphDatabase
from py2neo import Graph, Node, Relationship, Database,NodeMatcher

#graph = Graph()
#driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "1234"), encrypted=False)
#db=Graph("http://neo4j:1234@127.0.0.1:7474/db/data")


#ESTE CUESTIONARIO LO AGREGAMOS AL FINAL
# uri=input("¡Es hora de iniciar! ¿Cual es su URI?}\n")
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

# here we create our database. we start with the three main nodes
brawler = Node("Style", name="Brawler")
swordfighter = Node("Style", name="Swordfighter")
gunner = Node("Style", name="Gunner")

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

    #we upload them to the database one by one  
    c=characterDict[character]
    db.create(c)
