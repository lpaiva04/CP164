"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

# Code
food = open("foods.txt", "r")
print ("Queue: ")
qp = Priority_Queue()
qp.insert(food.readline())
qp.insert(food.readline())
for i in qp:
    print (i)
print ("Remove Priority Value:")
qp.remove()
for i in qp:
    print (i)
