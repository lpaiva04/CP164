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
from utilities import array_to_list, list_to_array
from List_array import List
# Code
source = [1, 2, 3, 4, 5]
llist = List()

array_to_list(llist, source)
print (f"Array to list:")
for i in llist:   
    print (i)
print ("----------------")
llist = List()
for i in range(1, 11):
    llist.append(i)
target = []

list_to_array(llist, target)

print (f"List to array:")
print (target)


