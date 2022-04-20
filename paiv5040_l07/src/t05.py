"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Code

list1 = List()
list2 = List()
target = List()

list1.append(1)
list1.append(2)
list1.append(3)

list2.append(1)
list2.append(2)
list2.append(4)

target.union(list1, list2)

for i in target:
    print (i)
