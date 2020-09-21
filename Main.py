import GenerateDatabase as database

"""
Main.py
------------------
Main file to generate SmashMain Database from a CSV
------------------
Authors: 
    Isabel Ortiz        18176
    Douglas De León     18037
    Pablo Ruiz          18259
    
Adapted from Main.py by: 
    Alejandro Álvarez   12429
    Joonho Kim          18096
    Pablo Ruiz          18259
    
Date: 
      21.09.2020
Version: 
      1.1.0
"""


# Deletes previous database versions if present
database.delete()

# Generates the initial database
database.generateDatabase()
