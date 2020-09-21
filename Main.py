import GenerateDatabase as database

"""
Main.py
------------------
Main file to run the Smash Bros Main Recommendation
------------------
Authors: 

Date: 
      30.05.2020
Version: 
      1.0.0
"""


# Deletes previous database versions if present
database.delete()

# Generates the initial database
database.generateDatabase()
