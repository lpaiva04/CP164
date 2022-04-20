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

list.prepend(1)
list.prepend(2)
list.prepend(3)

for i in list:
    print (i)
print ("-----------------------")
list = List()

list.append(1)
list.append(2)
list.append(3)

for i in list:
    print (i)
print ("-----------------------")

list.insert(1, 99)
for i in list:
    print (i)