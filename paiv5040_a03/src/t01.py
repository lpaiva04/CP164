"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from Stack_array import Stack

# Code

source1 = Stack()
source2 = Stack()

n = 5

for i in range(n):
    value = int(input("Enter a value: "))
    source1.push(value)
    source2.push(value)
    
source2.push(20)
source2.push(7)

target = stack_combine(source1, source2)

for i in target:
    print (i)