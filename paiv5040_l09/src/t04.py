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

HS.debug()

HS._rehash()
print ("-----------------------------")
print ("Rehashed Version:")
HS.debug()