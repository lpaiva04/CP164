"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-15"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods

# Code
file_variable = open("foods.txt", "r")

foods = []
line = file_variable.readline()

while line != "":
    food = line
    foods.append(food)
    line = file_variable.readline()

file = write_foods(file_variable, foods)

print (file)