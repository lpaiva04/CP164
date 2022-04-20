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
from Food_utilities import read_foods
from Food_utilities import by_origin

# Code
file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
origin = int(input("enter the food's origin(int): "))

origins = by_origin(foods, origin)

for i in origins:
    print (i)
