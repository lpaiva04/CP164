"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-02-04"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import list_test
# Code
file = open("foods.txt", "r")
source = []
i = 0
while i <= 10:
    source.append(file.readline())
    i += 1
    
list_test(source)


