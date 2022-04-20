"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-24"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Code

bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(-1)

zero, one, two = bst.node_counts()
print ("node_counts:")
print (f"Zero: {zero}")
print (f"One: {one}")
print (f"Two: {two}")
print ("-------------------")
print ("__contains__:")

print (bst.__contains__(1))
print (bst.__contains__(99))
print ("-------------------")
print ("parent (iterative)")

print (f"Parent of node with value == 4: {bst.parent(4)}")


print ("-------------------")
print ("parent (recursive)")

print (f"Parent of node with value == 4: {bst.parent_r(4)}")
