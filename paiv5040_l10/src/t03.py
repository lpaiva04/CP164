"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-26"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import test_sort, SORTS, SIZE

# Code
print (f"n:    {SIZE}         |       Comparisons     |   |                 Swap                  |")
print ("Algorithm         In Order Reversed Random    In Order        Reveres            Random")

print ("--------------    -------- -------  --------  --------        --------         --------")

for i in SORTS:
    title = i[0]
    func = i[1]
    test_sort(title, func)