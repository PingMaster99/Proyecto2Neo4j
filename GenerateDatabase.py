import csv
from neo4j import GraphDatabase
from py2neo import Graph, Node, Relationship

#graph = Graph()
driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "1234"))