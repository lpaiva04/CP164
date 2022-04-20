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

# Code

source = List()
for i in range(1, 11):
    source.append(i)

value = source[3]
print ("List:")
for i in source:
    print (i)
print (f"Value at 3rd index of list: {value}")

source[3] = 99

print (f"Replace value at 3rd index with 99:")

for i in source:
    print (i)
