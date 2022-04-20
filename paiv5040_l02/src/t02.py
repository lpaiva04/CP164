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
from utilities import array_to_stack
from Stack_array import Stack
# Code
source = [1, 2, 3, 4, 5, 6, 7, 8]

stack = Stack()
array_to_stack(stack, source)

for i in stack:
    print (i)