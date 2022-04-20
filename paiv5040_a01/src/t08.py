"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-10"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

# Code
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

small, large, total, average = matrix_stats(a)

print (a)
print (f"Smallest number: {small}")
print (f"Largest number: {large}")
print (f"Total value: {total}")
print (f"Average value: {average}")

