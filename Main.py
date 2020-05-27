import csv
from neo4j import GraphDatabase
from py2neo import Graph, Node, Relationship

#graph = Graph()
driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "1234"))

# graph.run("CREATE (n:Person { name: 'Andy', title: 'Developer' })")
#
# graph.close()

with open('smashCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    characterDict = {}
    for row in csv_reader:
        characterDict[row[0]] = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]

characterDict.pop("Name")

# here we create our database. we start with the three main nodes
brawler = Node("Style", name="Brawler")
swordfighter = Node("Style", name="Swordfighter")
gunner = Node("Style", name="Gunner")

bs = Relationship(brawler, "connectedTo", swordfighter)
bg = Relationship(brawler, "connectedTo", gunner)
sg = Relationship(gunner, "connectedTo", swordfighter)

for character in characterDict:
    # print(characterDict[character][1])
    if characterDict[character][1] == "Projectile":
        a = Relationship(characterDict[character], "is", gunner)
        print(a)

    if characterDict[character][1] == "Brawler":
        a = Relationship(characterDict[character], "is", brawler)
        print(a)

    if characterDict[character][1] == "Sword":
        a = Relationship(characterDict[character], "is", swordfighter)
        print(a)

    characterDict[character] = Node("Character", name=characterDict[character][0], style=characterDict[character][1],
                                    oos=characterDict[character][2], weight=characterDict[character][3],
                                    tier=characterDict[character][4], jumps=characterDict[character][5],
                                    saga=characterDict[character][6], types=characterDict[character][7])
    # graph.create(characterDict[character])
