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
from Food_utilities import calories_by_origin

# Code
file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
origin = int(input("Enter the origin(int): "))

avg = calories_by_origin(foods, origin)

print (avg)