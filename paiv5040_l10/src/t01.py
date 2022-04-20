"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-26"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import create_randoms, create_reversed, create_sorted

# Code
print ("Reversed List:")
list = create_reversed()
for i in list:
    print(i)
print ("---------------------------")
print ("Sorted List:")
list2 = create_sorted()
for i in list2:
    print(i)
print ()
print ("---------------------------")
print ("Random List:")
lists = create_randoms()
for i in lists:
    for j in i:
        print (j)