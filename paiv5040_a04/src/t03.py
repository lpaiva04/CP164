"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

# Code
queue = Queue()
for i in range(0, 9):
    queue.insert(i)
print ("queue:")
for i in queue:
    print (i) 
print ("-------------------")   
target1, target2 = queue.split_alt()

print ("Target 1:")
for i in target1:
    print (i)
print ("-------------------")
print ("Target 2:")
for i in target2:
    print (i)