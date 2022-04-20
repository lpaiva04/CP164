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
from test_Sorts_array import test_sort, SORTS

# Code
print ("Title             Sorted   Reversed Random    Swaps_sorted    Swaps_reversed     Swaps_random   ")
print ("")
for i in SORTS:
    test_sort(i[0], i[1])
