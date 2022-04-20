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
from functions import matrix_transpose

# Code

a = [[2, 4],[6, 8],[10, 12], [14, 16]]

b = matrix_transpose(a)

print (f"Original matrix: {a}")
print (f"Transposed matrix: {b}")
