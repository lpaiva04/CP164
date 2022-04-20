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
key = 99
source = List()
for i in range(1, 11):
    source.append(i)
print ("List:")
for i in source:
    print (i)
print ("---------------------------------")
source.insert(5, 99)
print ("Insert 99 at 5th index: ")
for i in source:
    print (i)
print ("---------------------------------")
print ("Remove key value (99) from list:")
source.remove(key)
for i in source:
    print (i)


