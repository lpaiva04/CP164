"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-02-26"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Code
list = List()
list.append(1)
list.append(2)
list.append(3)
for i in list:
    print (i)
print ("-----------------")
print (f"Return 3: {list.find(3)}")
print (f"Index of 1 in list: {list.index(1)}")
print (f"List contains 2: {list.__contains__(2)}")
