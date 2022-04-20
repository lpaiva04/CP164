"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_table
from Food_utilities import read_foods

# Code
file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)

food_table(foods)