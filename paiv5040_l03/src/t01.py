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
from Queue_array import Queue

# Code

queue = Queue()
queue.insert(0)
for i in queue:
    print (i)
print ("Insert 7 to rear:")
queue.insert(7)
for i in queue:
    print (i)