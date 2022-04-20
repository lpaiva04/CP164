"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-18"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Code

bst1 = BST()
bst2 = BST()

print ("is_balanced:")

print (bst1.is_balanced())

print ("--------------------")
print ("is_valid:")

print (bst1.is_valid())

print ("--------------------")
print ("Is_identical:")

print (bst1.is_identical(bst2))

print ("--------------------")
print ("Min:")

bst1.insert(10)
print (bst1.min())

print ("--------------------")
print ("Leaf_count:")

print (bst1.leaf_count())

print ("--------------------")
print ("One_child_count:")

print (bst1.one_child_count())

print ("--------------------")
print ("two_child_count:")

bst1.insert(1)
bst1.insert(2)
bst1.insert(3)
bst1.insert(4)

print (bst1.two_child_count())

print ("--------------------")
print ("Inorder")

print (bst1.inorder())

print ("--------------------")
print ("preorder")

print (bst1.preorder())
print ("--------------------")
print ("postorder")

print (bst1.postorder())

print ("--------------------")
print ("levelorder")

print (bst1.levelorder())

print ("--------------------")
print ("Remove:")

print (bst1.remove(1))

print ("--------------------")