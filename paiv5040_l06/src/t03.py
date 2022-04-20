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
print (f"Count of empty list: {list.count(5)}")
list.append(5)
print (f"New count of 5 after appending 5: {list.count(5)}")
print ("------------------")
list.append(1)
list.append(9)
print (f"Max value: {list.max()}")
print (f"Min Value: {list.min()}")