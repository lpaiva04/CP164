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
key = 8
source = List()
for i in range(1, 11):
    source.append(i)
print ("List:")
for i in source:
    print (i)
print ("-----------------------------------------")
print (f"Index of key: {source.index(key)}")
print (f"Key value in list (-1 if not present): {source.find(key)}")
print (f"Number of times key appears in the list: {source.count(key)}")
print (f"Largest value in list: {source.max()}")
print (f"Smallest value in list: {source.min()}")
