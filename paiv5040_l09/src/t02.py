"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

# Code

HS = Hash_Set(5)

print ("Insert 1, 2, 3: ")

HS.insert(1)
HS.insert(2)
HS.insert(3)

for i in HS:
    print (i)

print ("-------------------")
print ("Remove 1:")

print (HS.remove(1))
print ("-------------------")
print ("Remaining List:")

for i in HS:
    print (i)
