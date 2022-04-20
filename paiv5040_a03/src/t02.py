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
from Stack_array import Stack

# Code

source1 = []
source2 = []
target = Stack()
n = 5

for i in range(n):
    value = int(input("Enter a value: "))
    source1.append(value)
    source2.append(value)
    
source2.append(20)
source2.append(7)

target.combine(source1, source2)

for i in target:
    print (i)