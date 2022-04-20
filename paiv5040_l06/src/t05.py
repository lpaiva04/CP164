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
print (f"Last value in list: {list.peek()}")
print (f"Remove 2: {list.remove(2)}")
print ("List after removing 2:")
for i in list:
    print (i)