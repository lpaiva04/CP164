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
from Food_utilities import read_food

# Code
line = "Spanakopita|5|True|260"


food = read_food(line)

print (food)