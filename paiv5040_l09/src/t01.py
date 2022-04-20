"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Food_utilities import read_foods

# Code
fh = open("foods.txt", "r")
foods = read_foods(fh)

hash_table(1, foods)