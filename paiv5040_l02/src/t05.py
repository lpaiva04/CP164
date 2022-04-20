"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test

# Code

foods = open("foods.txt", "r")
line = foods.readline()
source = []
while line != "":
    source.append(line)
    line = foods.readline()
     
    
stack_test(source)