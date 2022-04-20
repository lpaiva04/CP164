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
from Food_utilities import food_search
from Food_utilities import read_foods

# Code
file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)

origin = int(input("Enter the origin(int): "))
max_cals = int(input("Enter the max calories(int): "))
is_veg = str(input("Is it vegetarian(Y/N): "))
result = food_search(foods, origin, max_cals, is_veg)

for i in result:
    print (i)