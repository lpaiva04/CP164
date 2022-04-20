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
from utilities import stack_to_array
from Stack_array import Stack

# Code
target = []

stack = Stack()

stack_to_array(stack, target)

print (target)

for i in stack:
    print (i)