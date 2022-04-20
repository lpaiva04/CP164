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
from Queue_circular import Queue
from functions import queue_split_alt 

# Code
source = Queue()
for n in range(0,9):
    source.insert(n)
print ("Source:")
for i in source:
    print (i) 
print ("-------------------")   
target1, target2 = queue_split_alt(source) 
print ("Target 1:")
for i in target1:
    print (i)
print ("-------------------")
print ("Target 2:")
for i in target2:
    print (i)

