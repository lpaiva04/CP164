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
print (f"Remove value at 1st index: {list[1]}")

list[1] = 99
print (f"Insert 99 to 1st position:")
for i in list:
    print (i)