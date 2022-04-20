"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-09"
-------------------------------------------------------
"""
# Imports
from functions import clean_list

# Code
values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4, 3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]

print (f"Values: {values}")

clean_list(values)

print (f"Cleaned: {values}")